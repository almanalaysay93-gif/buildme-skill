#!/usr/bin/env python3
"""Keyless, network-free checks of the approved public site's built HTML."""

import argparse
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


LIMIT = 2 * 1024 * 1024
UPSTREAM_REF = "6be93f45064ffbadced572b5d5c95f55fd263af0"


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.headings = 0
        self.meta = {}
        self.canonicals = []
        self.images = []
        self.schemas = []
        self.schema_buffer = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.headings += 1
        elif tag == "meta":
            key = (attrs.get("name") or attrs.get("property") or "").lower()
            self.meta.setdefault(key, []).append(attrs.get("content") or "")
        elif tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonicals.append(attrs.get("href") or "")
        elif tag == "img":
            self.images.append(attrs)
        elif tag == "script" and (attrs.get("type") or "").lower() == "application/ld+json":
            self.schema_buffer = ""

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.schema_buffer is not None:
            self.schema_buffer += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.schema_buffer is not None:
            self.schemas.append(self.schema_buffer)
            self.schema_buffer = None


def read_local(root, path):
    target = path.resolve()
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError("Artifact is missing or outside the approved site directory")
    if target.stat().st_size > LIMIT:
        raise ValueError("Artifact exceeds the 2 MiB inspection limit")
    return target.read_text(encoding="utf-8")


def public_origin(url):
    parsed = urlparse(url)
    try:
        parsed.port
    except ValueError as error:
        raise ValueError("Invalid public base URL") from error
    if (parsed.scheme not in ("https", "http") or not parsed.hostname
            or parsed.username or parsed.password or parsed.query or parsed.fragment
            or parsed.path not in ("", "/")):
        raise ValueError("Use a public HTTP(S) site origin without credentials, path, query or fragment")
    return url.rstrip("/") + "/"


def audit(site_dir, base_url, audience="public", pages=None, max_pages=50,
          require_schema=False, product_schema=False):
    report = {"scope": "built-artifacts-only", "audience": audience,
              "upstream": f"AgriciDaniel/claude-seo@{UPSTREAM_REF}",
              "checks": [], "pages": [], "pending": [], "limitations": [
                  "No network requests, API calls, accounts or model services are used.",
                  "Built HTML cannot prove rendered SPA content, HTTP headers, redirects, indexation or real-user performance.",
                  "JSON-LD syntax checks are not a complete Schema.org or rich-result eligibility validator."]}
    if audience != "public":
        report.update(static_status="NOT_APPLICABLE", overall_status="NOT_APPLICABLE")
        report["limitations"].append("SEO scope excluded; functional, mobile and accessibility gates still apply.")
        return report
    root = Path(site_dir).resolve()
    if not root.is_dir():
        raise ValueError("Built site directory is missing")
    base_url = public_origin(base_url)
    if max_pages < 1:
        raise ValueError("max-pages must be positive")
    findings = report["checks"]

    def check(rule, page, passed, evidence, fix, owner="Agent 2", required=True):
        findings.append({"id": rule, "page": page, "status": "PASS" if passed else "FAIL" if required else "WARN",
                         "severity": "High" if required else "Medium", "evidence": evidence,
                         "fix": "" if passed else fix, "suggested_owner": owner})

    selected = ([root / name for name in pages] if pages else sorted(root.rglob("*.html")))
    selected = list(dict.fromkeys(selected))
    check("html.present", "site", bool(selected), f"{len(selected)} HTML artifacts selected",
          "Provide built HTML or approved rendered HTML; SPA source alone needs browser validation.")
    if len(selected) > max_pages:
        report["pending"].append("Coverage incomplete: selected page count exceeds max-pages.")
    product_validator = None
    if product_schema:
        path = Path(__file__).resolve().parents[1] / "vendor/claude-seo/scripts/schema_ecommerce_validate.py"
        spec = importlib.util.spec_from_file_location("claude_seo_product", path)
        product_validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(product_validator)
    for path in selected[:max_pages]:
        try:
            html = read_local(root, path)
        except (ValueError, OSError, UnicodeError) as error:
            check("artifact.readable", "selected-artifact", False, str(error), "Supply an accessible in-scope UTF-8 artifact.")
            continue
        relative = path.resolve().relative_to(root).as_posix()
        route = relative[:-10] if relative.endswith("index.html") else relative
        url = urljoin(base_url, route)
        report["pages"].append(relative)
        page = Page(html)
        check("title.present", relative, bool(page.title.strip()), "Title present" if page.title.strip() else "No nonempty title",
              "Agent 9 supplies an accurate title; Agent 2 implements it.", "Agent 9")
        check("description.present", relative, any(x.strip() for x in page.meta.get("description", [])),
              "Checked description metadata", "Write an accurate page description.", "Agent 9", required=False)
        check("mobile.viewport", relative, any(re.search(r"width\s*=\s*device-width", x, re.I)
                                              for x in page.meta.get("viewport", [])),
              "Checked viewport width=device-width", "Set responsive viewport metadata and verify actual mobile behavior.")
        robots = ",".join(page.meta.get("robots", []) + page.meta.get("googlebot", [])).lower()
        check("indexing.public-page", relative, not {"noindex", "none"}.intersection(re.split(r"[,\s]+", robots)),
              "Checked index directives for an approved public page", "Remove accidental noindex or exclude the private route from approved SEO scope.")
        check("heading.primary", relative, page.headings > 0, f"{page.headings} h1 elements",
              "Review semantic page hierarchy.", required=False)
        canonical_ok = len(page.canonicals) == 1 and urlparse(page.canonicals[0]).scheme in ("http", "https")
        check("canonical.review", relative, canonical_ok, f"{len(page.canonicals)} canonical declarations",
              "Review canonical policy; use one appropriate absolute canonical URL.", required=False)
        if canonical_ok:
            check("canonical.origin", relative, urlparse(page.canonicals[0]).netloc == urlparse(base_url).netloc,
                  "Compared canonical host with approved site origin", "Confirm intentional cross-domain canonical or correct it.", required=False)
        missing_alt = sum("alt" not in image for image in page.images)
        check("images.alt", relative, missing_alt == 0, f"{missing_alt} images lack an alt attribute",
              "Add meaningful alt text or an empty alt for decorative images; audit in the browser.", required=False)
        missing_size = sum(not image.get("width") or not image.get("height") for image in page.images)
        check("images.dimensions", relative, missing_size == 0, f"{missing_size} images lack explicit dimensions",
              "Reserve space using dimensions or verified CSS aspect-ratio.", required=False)
        check("schema.present", relative, bool(page.schemas), f"{len(page.schemas)} JSON-LD blocks",
              "Supply applicable fact-grounded schema or document why none is needed.", required=require_schema or product_schema)
        schema_payloads = []
        for index, block in enumerate(page.schemas):
            try:
                data = json.loads(block)
                if not isinstance(data, (dict, list)) or not data:
                    raise ValueError("JSON-LD must contain an object or nonempty array")
            except (ValueError, RecursionError):
                check("schema.json", relative, False, f"JSON-LD block {index + 1} is invalid",
                      "Repair JSON-LD syntax and structure; confirm content matches the page.")
                continue
            check("schema.json", relative, True, f"JSON-LD block {index + 1} parses", "")
            schema_payloads.append(data)
        if product_validator and schema_payloads:
            try:
                result = product_validator.validate(schema_payloads)
                for item in result["findings"]:
                    check("product." + item["rule"], relative, False, item["message"],
                          "Review against current official Product documentation and approved catalog facts.",
                          required=item["severity"] in ("Critical", "High"))
            except (ValueError, TypeError, AttributeError, RecursionError):
                check("product.structure", relative, False, "Product schema could not be validated",
                      "Repair schema types and obtain a manual schema review.")
        robots_path = root / "robots.txt"
        if robots_path.exists():
            try:
                rules = RobotFileParser()
                rules.parse(read_local(root, robots_path).splitlines())
                check("robots.public-route", relative, rules.can_fetch("Googlebot", url),
                      "Checked local robots.txt against the selected public route",
                      "Correct accidental crawling restrictions; robots.txt is not authentication.")
            except (ValueError, OSError, UnicodeError) as error:
                check("robots.readable", relative, False, str(error), "Repair local robots.txt.")
    sitemap_path = root / "sitemap.xml"
    if sitemap_path.exists():
        try:
            xml = read_local(root, sitemap_path)
            if re.search(r"<!\s*(DOCTYPE|ENTITY)", xml, re.I):
                raise ValueError("DTD/entity declarations are unsupported")
            tree = ET.fromstring(xml)
            if tree.tag.split("}")[-1] not in ("urlset", "sitemapindex"):
                raise ValueError("Expected sitemap urlset or sitemapindex")
            locations = [node.text or "" for node in tree.iter() if node.tag.split("}")[-1] == "loc"]
            check("sitemap.structure", "site", bool(locations) and all(urlparse(x.strip()).scheme in ("https", "http")
                                                                       and urlparse(x.strip()).netloc for x in locations),
                  f"{len(locations)} sitemap locations checked", "Use valid sitemap XML and absolute HTTP(S) locations.")
        except (ValueError, ET.ParseError, OSError, UnicodeError) as error:
            check("sitemap.structure", "site", False, str(error), "Repair sitemap XML.")
    else:
        check("sitemap.discovery", "site", False, "No root sitemap.xml artifact inspected",
              "Inspect configured sitemap declarations/index routes at runtime; absence here is not proof no sitemap exists.", required=False)
    report["pending"] += ["Agent 10: browser/mobile/keyboard checks and local Lighthouse evidence.",
                           "Agent 6: served status, headers, redirects, crawlability, sitemap discovery and rendered-content/schema review."]
    report["static_status"] = "FAIL" if any(x["status"] == "FAIL" for x in findings) else "PASS"
    report["overall_status"] = "FAIL" if report["static_status"] == "FAIL" else "BLOCKED"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path)
    parser.add_argument("--base-url")
    parser.add_argument("--audience", choices=("public", "private", "native"), default="public")
    parser.add_argument("--page", action="append", help="Approved relative HTML artifact; repeat to scope public routes")
    parser.add_argument("--max-pages", type=int, default=50)
    parser.add_argument("--require-schema", action="store_true")
    parser.add_argument("--product-schema", action="store_true", help="Run bundled Claude SEO Product validator")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.audience == "public" and (args.site_dir is None or args.base_url is None):
        parser.error("public scope requires --site-dir and --base-url")
    try:
        result = audit(args.site_dir, args.base_url, args.audience, args.page,
                       args.max_pages, args.require_schema, args.product_schema)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Static SEO: {result['static_status']}; overall: {result['overall_status']}. Report: {args.output}")
    # Exit zero means these artifact checks finished, not that runtime SEO passed.
    return 1 if result["static_status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

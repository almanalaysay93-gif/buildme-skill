"""Test actual free SEO artifacts, applicability and worker-repair evidence."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/buildme/scripts/free_seo_audit.py"
SPEC = importlib.util.spec_from_file_location("free_seo_audit", SCRIPT)
seo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(seo)

GOOD = '''<!doctype html><html><head><title>Campus admissions</title>
<meta name="description" content="Find the admissions process and apply.">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://school.test/">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Campus"}</script>
</head><body><h1>Admissions</h1><a href="/apply">Apply</a></body></html>'''


class ArtifactAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="buildme-seo-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "index.html").write_text(GOOD)
        (self.root / "robots.txt").write_text("User-agent: *\nAllow: /\n")
        (self.root / "sitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            '<url><loc>https://school.test/</loc></url></urlset>')

    def audit(self, **kwargs):
        with patch("socket.socket", side_effect=AssertionError("SEO artifact audit must not open a network socket")):
            return seo.audit(self.root, "https://school.test", **kwargs)

    def failed(self, result, rule):
        return any(x["id"] == rule and x["status"] == "FAIL" for x in result["checks"])

    def test_good_artifacts_do_not_fake_runtime_pass(self):
        report = self.audit()
        self.assertEqual(report["static_status"], "PASS")
        self.assertEqual(report["overall_status"], "BLOCKED")
        self.assertTrue(report["pending"])

    def test_accidental_noindex_and_googlebot_directives_fail(self):
        for name in ["robots", "googlebot"]:
            with self.subTest(name=name):
                (self.root / "index.html").write_text(GOOD.replace("</head>", f'<meta name="{name}" content="noindex, follow"></head>'))
                self.assertTrue(self.failed(self.audit(), "indexing.public-page"))

    def test_robots_blocks_are_checked_against_actual_route(self):
        (self.root / "robots.txt").write_text("User-agent: Googlebot\nDisallow: /\n")
        self.assertTrue(self.failed(self.audit(), "robots.public-route"))

    def test_private_and_native_skip_seo_not_global_qa(self):
        for audience in ["private", "native"]:
            report = seo.audit(None, None, audience=audience)
            self.assertEqual(report["overall_status"], "NOT_APPLICABLE")
            self.assertIn("functional, mobile and accessibility", " ".join(report["limitations"]))

    def test_mobile_viewport_missing_is_actionable(self):
        (self.root / "index.html").write_text(GOOD.replace("width=device-width", "width=1200"))
        report = self.audit()
        self.assertTrue(self.failed(report, "mobile.viewport"))
        finding = next(x for x in report["checks"] if x["id"] == "mobile.viewport")
        self.assertEqual(finding["suggested_owner"], "Agent 2")
        self.assertTrue(finding["fix"])

    def test_broken_json_ld_is_not_silently_ignored(self):
        (self.root / "index.html").write_text(GOOD.replace('"name":"Campus"', '"name":INVALID'))
        self.assertTrue(self.failed(self.audit(), "schema.json"))

    def test_schema_missing_only_required_when_agreed(self):
        (self.root / "index.html").write_text('<title>Plain page</title><meta name="viewport" content="width=device-width"><h1>Plain</h1>')
        self.assertFalse(self.failed(self.audit(), "schema.present"))
        self.assertTrue(self.failed(self.audit(require_schema=True), "schema.present"))
        self.assertTrue(self.failed(self.audit(product_schema=True), "schema.present"))

    def test_upstream_product_validator_combines_json_ld_blocks(self):
        product = {"@context": "https://schema.org", "@type": "Product", "name": "Course materials",
                   "image": "https://school.test/book.webp", "offers": {"@type": "Offer", "price": "10",
                   "priceCurrency": "USD", "availability": "https://schema.org/InStock"}}
        html = GOOD.replace("</head>", '<script type="application/ld+json">' + json.dumps(product) + '</script></head>')
        (self.root / "index.html").write_text(html)
        report = self.audit(product_schema=True)
        self.assertFalse(self.failed(report, "product.missing-product"))
        self.assertEqual(report["static_status"], "PASS")
        product.pop("offers")
        (self.root / "index.html").write_text(GOOD.replace("</head>", '<script type="application/ld+json">' + json.dumps(product) + '</script></head>'))
        self.assertTrue(self.failed(self.audit(product_schema=True), "product.missing-product-offers"))

    def test_invalid_sitemap_is_a_failure(self):
        (self.root / "sitemap.xml").write_text("<html>SPA fallback</html>")
        self.assertTrue(self.failed(self.audit(), "sitemap.structure"))

    def test_sitemap_entity_declarations_are_refused(self):
        (self.root / "sitemap.xml").write_text('<!DOCTYPE x [<!ENTITY x "expansion">]><urlset/>')
        self.assertTrue(self.failed(self.audit(), "sitemap.structure"))

    def test_page_cap_reports_incomplete_coverage(self):
        (self.root / "about.html").write_text(GOOD)
        report = self.audit(max_pages=1)
        self.assertEqual(len(report["pages"]), 1)
        self.assertTrue(any("Coverage incomplete" in text for text in report["pending"]))

    def test_traversal_does_not_read_outside_approved_output(self):
        with tempfile.TemporaryDirectory() as other:
            secret = Path(other) / "not-approved.html"
            secret.write_text("should not appear in a report")
            report = self.audit(pages=[str(secret)])
            self.assertTrue(self.failed(report, "artifact.readable"))
            self.assertNotIn("should not appear", json.dumps(report))

    def test_credentialed_base_url_is_refused(self):
        with self.assertRaisesRegex(ValueError, "without credentials"):
            seo.audit(self.root, "https://user:secret@school.test")

    def test_cli_failure_fix_and_reaudit_preserves_runtime_blocker(self):
        report_path = self.root / "reports/seo.json"
        command = [sys.executable, str(SCRIPT), "--site-dir", str(self.root),
                   "--base-url", "https://school.test", "--output", str(report_path)]
        (self.root / "index.html").write_text(GOOD.replace("</head>", '<meta name="robots" content="noindex"></head>'))
        failed = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(failed.returncode, 1, failed.stderr)
        self.assertEqual(json.loads(report_path.read_text())["overall_status"], "FAIL")
        (self.root / "index.html").write_text(GOOD)
        fixed = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(fixed.returncode, 0, fixed.stderr)
        self.assertEqual(json.loads(report_path.read_text())["static_status"], "PASS")
        self.assertEqual(json.loads(report_path.read_text())["overall_status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()

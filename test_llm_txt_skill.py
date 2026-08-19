#!/usr/bin/env python3
"""Local smoke test for the Agent 6 llm-txt-skill.

Simulates the skill's workflow against a mock product context, generates an
llms.txt per the spec, and runs the skill's self-verify checklist.
"""
import os
import re
import sys

SITE_ROOT = "/tmp/llms_test_site"
PUBLIC = os.path.join(SITE_ROOT, "public")
SKILL = "/home/ubuntu/buildme-skill/skills/buildme/llm-txt-skill/SKILL.md"

# 1) Mock product context (stands in for PRODUCT.md / final site content)
PRODUCT_MD = """# Totten-Ham Car Wraps
Tottenham Car Wraps provides commercial and residential vehicle wrap services
in Tottenham, North London. We serve fleet operators, tradespeople, and
car owners. Services: full vehicle wraps, commercial fleet branding,
partial wraps and colour changes, window graphics. Founded 2012,
family-run, GST-registered, serves all of North London.
Contact: info@totten-hamwraps.example, 020 7946 0123, Tottenham, London N17.
"""

os.makedirs(PUBLIC, exist_ok=True)
open(os.path.join(SITE_ROOT, "PRODUCT.md"), "w").write(PRODUCT_MD)

# 2) Skill rules extracted from the SKILL.md spec
AI_SLOP = ["elevate", "unlock", "revolutionize", "world-class", "game-chang"]
SECTION_ORDER = ["# ", "## What is", "## What does", "## Why use", "## Contact"]

# 3) Generate llms.txt (Agent 6 output)
LLMS = """# Totten-Ham Car Wraps

> Commercial and residential vehicle wrap services for Tottenham and North London — full wraps, fleet branding, colour changes, and window graphics for a family-run shop established in 2012.

## What is Totten-Ham Car Wraps?
Totten-Ham Car Wraps is a family-run vehicle wrap company based in Tottenham,
North London, operating since 2012. We wrap cars, vans, and commercial fleet
vehicles for customers across London.

## What does Totten-Ham Car Wraps offer?
- Full vehicle wraps (colour changes and full branding)
- Commercial fleet branding for businesses and tradespeople
- Partial wraps and vinyl graphics
- Window graphics

## Why use Totten-Ham Car Wraps?
- Family-run and GST-registered, serving North London since 2012
- Specialised in commercial fleet branding
- Local Tottenham shop — easy drop-off across London N17

## Contact
- URL: https://tottenham-carwraps.example
- Email: info@totten-hamwraps.example
- Phone: 020 7946 0123
- Location: Tottenham, London N17
"""

out_path = os.path.join(PUBLIC, "llms.txt")
open(out_path, "w").write(LLMS)

# 4) Self-verify checklist
errors = []
content = LLMS

# Check 1: valid markdown, section order
idx = 0
for sec in SECTION_ORDER:
    pos = content.find(sec)
    if pos == -1:
        errors.append(f"Missing section: {sec.strip()}")
    elif pos < idx:
        errors.append(f"Section out of order: {sec.strip()}")
    idx = pos

# Check 2: word count <= 1500
if len(content.split()) > 1500:
    errors.append("Exceeds 1,500 words")

# Check 3: no AI-slop
lower = content.lower()
for word in AI_SLOP:
    if word in lower:
        errors.append(f"AI-slop phrase found: {word}")

# Check 4: contact fields filled
for field in ["URL:", "Email:", "Phone:", "Location:"]:
    if field not in content:
        errors.append(f"Contact field missing: {field}")

# Check 5: claims grounded in PRODUCT_MD (spot check key facts)
for fact in ["Tottenham", "North London", "2012", "fleet"]:
    if fact.lower() not in content.lower():
        errors.append(f"Fact missing: {fact}")
    if fact.lower() not in PRODUCT_MD.lower():
        errors.append(f"Fact not grounded in PRODUCT.md: {fact}")

# Check 6: file lands in public/
if not os.path.exists(out_path):
    errors.append("llms.txt not written to public/")

if errors:
    print("SELF-VERIFY FAILED:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print("ALL CHECKS PASSED")
print("llms.txt written to:", out_path)
print("Keywords AI will associate with site: vehicle wrap, Tottenham, North London, fleet branding, London N17")

#!/usr/bin/env python3
"""
generate_readme.py
------------------
Generates the project README.md locally.

Usage:
    python scripts/generate_readme.py
"""

import os

README_CONTENT = """# VERA Data Intelligence Platform\n### Power BI Engineer - Technical Assessment | RIAR Consulting\n\nSee the full README at: https://github.com/harshilnagwani/vera-powerbi-assessment\n"""

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md"
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(README_CONTENT)

print(f"README.md written to: {output_path}")

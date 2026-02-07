import json
import os
from datetime import datetime

# Configuration
BASE_URL = "https://100dmurphy.github.io/python-data-tools"
NAV_PATH = "webapp/src/lib/nav.json"
OUTPUT_PATH = "webapp/static/sitemap.xml"

def generate_sitemap():
    if not os.path.exists(NAV_PATH):
        print(f"Error: {NAV_PATH} not found.")
        return

    with open(NAV_PATH, "r") as f:
        nav_sections = json.load(f)

    # Collect all paths
    paths = ["/"] # Home
    for section in nav_sections:
        # Some sections might have a top-level path (if landing page exists)
        if "path" in section:
             # Just in case there are nested structures not in items
             pass
        
        for item in section["items"]:
            paths.append(item["path"])

    # Generate XML
    today = datetime.now().strftime("%Y-%m-%d")
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for path in sorted(set(paths)):
        url = f"{BASE_URL}{path}"
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>{url}</loc>')
        xml_content.append(f'    <lastmod>{today}</lastmod>')
        xml_content.append('    <changefreq>weekly</changefreq>')
        xml_content.append('    <priority>0.8</priority>')
        xml_content.append('  </url>')

    xml_content.append('</urlset>')

    with open(OUTPUT_PATH, "w") as f:
        f.write("\n".join(xml_content))

    print(f"Sitemap generated successfully: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_sitemap()

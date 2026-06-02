#!/usr/bin/env python3
"""
Generate statistics_data.json from markdown files in the statistics/ folder.
This script reads all .md files organized by chapter and creates a JSON structure
that the wireframe loader can consume.
"""

import os
import json
import re
from pathlib import Path

def extract_title_from_md(content):
    """Extract title from markdown file (first # heading)."""
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Untitled"

def extract_overview_from_md(content):
    """Extract overview section from markdown."""
    lines = content.split('\n')
    overview = []
    in_overview = False

    for line in lines:
        if '## Overview' in line:
            in_overview = True
            continue
        if in_overview and line.startswith('##'):
            break
        if in_overview and line.strip():
            overview.append(line.strip())

    return ' '.join(overview[:2]) if overview else "[Content placeholder]"

def get_image_paths(chapter_dir):
    """Get list of image files in the chapter's images/ folder."""
    images_dir = Path(chapter_dir) / 'images'
    images = []

    if images_dir.exists():
        for img_file in sorted(images_dir.glob('*')):
            if img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                # Store relative path from deploy root
                rel_path = f"statistics/{chapter_dir.name}/images/{img_file.name}"
                images.append(rel_path)

    return images

def generate_json_from_markdown():
    """Read markdown files and generate JSON structure."""

    statistics_dir = Path('statistics')

    if not statistics_dir.exists():
        print("Error: 'statistics' folder not found in current directory")
        return None

    data = {}
    chapter_num = 0

    # Iterate through chapter directories (01-*, 02-*, etc.)
    chapter_dirs = sorted([d for d in statistics_dir.iterdir() if d.is_dir() and re.match(r'^\d{2}-', d.name)])

    for chapter_dir in chapter_dirs:
        chapter_num += 1
        chapter_name = chapter_dir.name.split('-', 1)[1].replace('-', ' ').title()

        # Get markdown files in this chapter
        md_files = sorted([f for f in chapter_dir.glob('*.md') if f.name != 'README.md'])

        items = []

        for topic_num, md_file in enumerate(md_files, 1):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title_from_md(content)
            lede = extract_overview_from_md(content)

            # Get image paths for this topic
            images = get_image_paths(chapter_dir)

            item = {
                "id": md_file.stem,
                "number": f"{chapter_num}.{topic_num}",
                "title": title,
                "lede": lede,
                "sectionOneTitle": "Overview",
                "sectionOneBody": content[:500] + "..." if len(content) > 500 else content,
                "sectionTwoTitle": "Key Concepts",
                "sectionTwoBody": "[Add key concepts here]",
                "images": images,
                "md_file": f"statistics/{chapter_dir.name}/{md_file.name}"
            }

            items.append(item)

        data[f"chapter_{chapter_num}"] = {
            "number": str(chapter_num),
            "label": chapter_name,
            "items": items
        }

    return data

def main():
    print("Generating statistics_data.json from markdown files...")

    data = generate_json_from_markdown()

    if data is None:
        return

    output_file = Path('statistics_data.json')

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully generated {output_file}")
    print(f"   Chapters: {len(data)}")
    total_topics = sum(len(ch['items']) for ch in data.values())
    print(f"   Total topics: {total_topics}")

if __name__ == '__main__':
    main()

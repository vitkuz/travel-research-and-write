#!/usr/bin/env python3
"""
Save place research data to structured directory:
dist/[destination]/[place]/[date]/[place].json

Usage:
    python save_place_research.py --destination "Istanbul" --place "Süleymaniye Mosque" --data '{"place":"...",...}'
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def sanitize_folder_name(name: str) -> str:
    """
    Convert name to safe folder name:
    - Remove special characters except spaces and hyphens
    - Convert spaces to hyphens
    - Convert to lowercase
    - Remove consecutive hyphens
    """
    # Remove special characters, keep alphanumeric, spaces, and hyphens
    name = re.sub(r'[^\w\s-]', '', name)
    # Convert spaces to hyphens
    name = re.sub(r'\s+', '-', name)
    # Convert to lowercase
    name = name.lower()
    # Remove consecutive hyphens
    name = re.sub(r'-+', '-', name)
    # Strip leading/trailing hyphens
    name = name.strip('-')
    return name


def save_place_research(destination: str, place: str, data: dict) -> str:
    """
    Save place research JSON to dist/[destination]/[place]/[date]/[place].json
    
    Returns:
        str: Full path to saved file
    """
    # Sanitize names for folder structure
    destination_folder = sanitize_folder_name(destination)
    place_folder = sanitize_folder_name(place)
    
    # Get current date in YYYY-MM-DD format
    date_folder = datetime.now().strftime('%Y-%m-%d')
    
    # Build directory path
    output_dir = Path('dist') / destination_folder / place_folder / date_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON file (use original place name for filename)
    place_filename = sanitize_folder_name(place)
    output_file = output_dir / f'{place_filename}.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return str(output_file)


def main():
    parser = argparse.ArgumentParser(
        description='Save place research data to structured directory'
    )
    parser.add_argument(
        '--destination',
        required=True,
        help='Destination city/region (e.g., "Istanbul", "New York")'
    )
    parser.add_argument(
        '--place',
        required=True,
        help='Place name (e.g., "Süleymaniye Mosque")'
    )
    parser.add_argument(
        '--data',
        required=True,
        help='JSON string containing place research data'
    )
    
    args = parser.parse_args()
    
    # Parse JSON data
    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON data - {e}")
        return 1
    
    # Validate required fields
    required_fields = [
        'place', 'type', 'description', 'highlights', 'tips',
        'vibe', 'expectations', 'reality', 'unique_facts', 'surprises'
    ]
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        print(f"❌ Error: Missing required fields: {', '.join(missing_fields)}")
        return 1
    
    # Save the file
    try:
        output_path = save_place_research(args.destination, args.place, data)
        print(f"✅ Place research saved successfully!")
        print(f"📁 Location: {output_path}")
        return 0
    except Exception as e:
        print(f"❌ Error: Failed to save file - {e}")
        return 1


if __name__ == '__main__':
    exit(main())

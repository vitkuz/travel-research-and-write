---
name: destination-research
description: Research and compile top 10 places for travel destinations. Use when users request place recommendations, destination research, or want to explore what to visit in a specific location. Outputs structured JSON with place details including name, category, description, coordinates, rating, and visit rationale.
---

# Destination Research

Research destinations and compile the top 10 must-visit places into structured JSON output.

## Research Process

1. **Search for destination information** using web_search to find:
   - Popular tourist attractions
   - Cultural landmarks and historical sites
   - Natural wonders and viewpoints
   - Local experiences and hidden gems
   - Current travel recommendations

2. **Select top 10 places** based on:
   - Cultural significance and uniqueness
   - Visitor ratings and popularity
   - Diversity of experience types
   - Photogenic/video-worthy appeal
   - Accessibility and practical visitability

3. **Gather comprehensive details** for each place:
   - Official name and common variants
   - Category (e.g., "Cultural Site", "Natural Wonder", "Viewpoint", "Restaurant", "Beach", "Temple")
   - Concise description (1-2 sentences)
   - GPS coordinates (decimal format)
   - Rating (out of 5, if available)
   - Why visit (compelling 1-sentence rationale)

## Output Format

**CRITICAL: Output file structure is mandatory**

Save results to:
```
dist/[country]/places.json
```

**File path rules**:
- `[country]`: Lowercase country name, hyphens for spaces (e.g., "turkey", "united-states", "france")
- Filename: Always `places.json`

**Examples**:
- Turkey (Istanbul) → `dist/turkey/places.json`
- United States (New York City) → `dist/united-states/places.json`
- France (Paris) → `dist/france/places.json`

**Create the directory if it doesn't exist**:
```bash
mkdir -p dist/[country]
```

**JSON Schema:**

```json
{
  "destination": "string",
  "researched_at": "ISO-8601 timestamp",
  "places": [
    {
      "rank": "number (1-10)",
      "name": "string",
      "category": "string",
      "description": "string",
      "coordinates": {
        "lat": "number",
        "lng": "number"
      },
      "rating": "number (0-5, nullable)",
      "why_visit": "string"
    }
  ]
}
```

## Quality Standards

- Research must include web searches for current, accurate information
- Places should represent diverse experience types (not all temples, not all beaches)
- Coordinates must be accurate decimal format
- Descriptions should be travel-guide quality: informative yet engaging
- Rankings should reflect both popularity and unique value
- Each place must have all required fields populated

## Example Output Structure

```json
{
  "destination": "Bali",
  "researched_at": "2025-11-03T10:30:00Z",
  "places": [
    {
      "rank": 1,
      "name": "Tanah Lot Temple",
      "category": "Cultural Site",
      "description": "Ancient Hindu shrine perched on a dramatic offshore rock formation, dating back to the 16th century.",
      "coordinates": {
        "lat": -8.6211,
        "lng": 115.0869
      },
      "rating": 4.6,
      "why_visit": "Iconic sunset views and spiritual significance make this Bali's most photographed temple."
    }
  ]
}
```

## Complete Workflow Summary

1. **Receive destination request** from user
2. **Research using web_search** - minimum 5-7 searches for comprehensive data
3. **Select top 10 places** - diverse, significant, visually appealing
4. **Compile structured JSON** with all required fields
5. **Create directory structure**: `mkdir -p dist/[country]`
6. **Save file**: Write JSON to `dist/[country]/places.json`

## File Path Examples

- Input: "Istanbul" → Output: `dist/turkey/places.json`
- Input: "Bali" → Output: `dist/indonesia/places.json`
- Input: "New York City" → Output: `dist/united-states/places.json`
- Input: "São Paulo" → Output: `dist/brazil/places.json`
- Input: "Paris" → Output: `dist/france/places.json`

---
name: place-research
description: Research travel destinations and compile comprehensive place information including descriptions, highlights, tips, vibe, expectations vs reality, unique facts, and surprises. Use when users request detailed place research for travel content creation, destination guides, or need structured JSON output about specific locations (landmarks, attractions, neighborhoods, etc.).
---

# Place Research

Comprehensive destination research workflow that generates detailed, structured information about specific places.

## Workflow

### 1. Gather Input

Extract the following from the user's request:
- **Place name**: The specific location to research (e.g., "Süleymaniye Mosque", "Central Park")
- **Destination**: The city/region context (e.g., "Istanbul", "New York City")
- **Type**: The place category (cultural, natural, entertainment, historical, culinary, etc.)

If any information is missing, ask the user before proceeding.

### 2. Research Phase

Use web_search extensively to gather comprehensive information:

**Essential searches** (minimum 5-7 searches):
- "[place name] [destination]" - basic overview
- "[place name] history architecture details" - background
- "[place name] visitor tips best time to visit"
- "[place name] hidden features secrets"
- "[place name] visitor expectations vs reality"
- "[place name] unusual facts trivia"
- "[place name] local perspective neighborhood"

**Follow-up searches** as needed to fill gaps in:
- Architectural/design details
- Historical significance
- Visitor experiences and reviews
- Practical visiting information
- Local culture and context

### 3. Content Generation

Generate each JSON field with rich, specific content:

#### place
The exact name of the location.

#### type
Category: cultural, natural, entertainment, historical, culinary, shopping, spiritual, architectural, etc.

#### description (200-300 words)
Comprehensive overview covering:
- What it is and why it's significant
- Historical context and background
- Architectural/design features (if relevant)
- Current status (UNESCO site, restoration, etc.)
- Size, scale, or scope

#### highlights (6-10 items)
Specific, concrete features that make the place special:
- Use exact measurements, numbers, dates
- Focus on unique architectural/design elements
- Include notable art, artifacts, or collections
- Mention viewpoints, experiences, or activities
- Each highlight should be 1-2 detailed sentences

#### tips (8-12 items)
Actionable, practical advice for visitors:
- Best times to visit (specific hours/days)
- What to avoid (crowds, closures)
- Dress codes or entry requirements
- Photography tips
- Nearby complementary attractions
- Local food/drink recommendations near the place
- Money-saving advice
- How to combine with other activities

#### vibe (150-200 words)
Atmospheric description capturing:
- The emotional experience of being there
- Sensory details (light, sound, space, crowds)
- The overall feeling or energy
- How it compares to similar places
- What makes the atmosphere unique

#### expectations (5 items)
Common misconceptions or assumptions visitors have before arrival:
- Each should be a clear, specific expectation
- Cover assumptions about crowds, access, significance, experience, or appearance

#### reality (5 items)
The truth that counters each expectation:
- Match the order of expectations
- Provide specific, surprising corrections
- Use concrete details and comparisons
- Explain why the reality differs

#### unique_facts (8-12 items)
Fascinating, lesser-known information:
- Historical anecdotes and legends
- Engineering or construction details
- Notable connections to famous people/events
- Records or superlatives
- Unusual features or hidden details
- Each fact should surprise or intrigue

#### surprises (8-12 items)
Unexpected discoveries visitors encounter:
- Things that aren't mentioned in guidebooks
- Hidden features or details
- Surprising comparisons or contrasts
- Neighborhood or contextual surprises
- Unexpected practical benefits
- Charming local touches

### 4. Output Generation

**CRITICAL: Output file structure is mandatory**

Save the research JSON to:
```
dist/[country]/[place]/[date]/research.json
```

**File path rules**:
- `[country]`: Lowercase country name, hyphens for spaces (e.g., "turkey", "united-states", "france")
- `[place]`: Lowercase place name, hyphens for spaces (e.g., "hagia-sophia", "central-park")
- `[date]`: Current date in YYYY-MM-DD format (e.g., "2025-11-03")
- Filename: Always `research.json`

**Examples**:
- Istanbul, Süleymaniye Mosque → `dist/turkey/suleymaniye-mosque/2025-11-03/research.json`
- New York City, Central Park → `dist/united-states/central-park/2025-11-03/research.json`
- Paris, Louvre Museum → `dist/france/louvre-museum/2025-11-03/research.json`

**Create the directory structure if it doesn't exist**:
```bash
mkdir -p dist/[country]/[place]/[date]
```

**Then write the JSON file using the Write tool** with the complete research data structure.

## Quality Standards

**Depth over breadth**: Each section should contain rich, specific details rather than generic descriptions.

**Authenticity**: Research actual visitor experiences, not just official descriptions.

**Specificity**: Use exact numbers, dates, measurements, and names whenever possible.

**Balance**: Cover both positive aspects and practical realities.

**Local perspective**: Include neighborhood context and local culture.

**Actionability**: Tips should be specific enough to act on immediately.

## Output Format

The final JSON structure:

```json
{
  "place": "string",
  "type": "string",
  "description": "string (200-300 words)",
  "highlights": ["array of 6-10 detailed strings"],
  "tips": ["array of 8-12 actionable strings"],
  "vibe": "string (150-200 words)",
  "expectations": ["array of 5 assumption strings"],
  "reality": ["array of 5 reality strings, matching expectations order"],
  "unique_facts": ["array of 8-12 fascinating strings"],
  "surprises": ["array of 8-12 unexpected discovery strings"]
}
```

## Example Triggers

- "Research the Eiffel Tower for my travel guide"
- "I need detailed info about Central Park for a video script"
- "Build a place research file for the Colosseum"
- "Generate comprehensive destination content for Angkor Wat"

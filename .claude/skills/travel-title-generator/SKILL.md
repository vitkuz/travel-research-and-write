---
name: travel-title-generator
description: Generate and rank YouTube video titles for travel content using 100 proven formulas. Use when users need video titles, want title ideas for travel scripts/videos, or request titles for specific story files (e.g., dist/georgia/gonio-fortress/2025-11-04/script.md). Analyzes story emotion, recommends best formula categories, and outputs 15-20 ranked titles with fit scores.
---

# Travel Title Generator

Generate compelling, click-worthy YouTube titles for travel videos using proven formulas and Lilia's authentic voice.

---

## When to Use This Skill

Use this skill when:
- User requests video titles for a travel story/script
- User provides a path to a script file (e.g., `dist/[country]/[place]/[date]/script.md`)
- User wants title ideas or suggestions for travel content
- User mentions "generate titles", "create titles", "title options"
- User needs A/B testing variants for video titles
- User wants to explore different title approaches

---

## Workflow

### STEP 1: Load Reference Files

**MANDATORY - Load these in order:**

```
view references/title-formulas.md
```

```
view references/title-rating-guide.md
```

**Critical:** You MUST load these references before generating any titles. They contain the 100 formulas and rating criteria.

---

### STEP 2: Read and Analyze the Script

**Input:** User provides script path (e.g., `dist/georgia/gonio-fortress/2025-11-04/script.md`)

**Read the script and extract:**

1. **Place/Destination Information:**
   - Specific place name (e.g., "Gonio Fortress")
   - Country/region (e.g., "Georgia")
   - Place type (fortress, market, neighborhood, natural site, etc.)

2. **Emotional Arc Analysis:**
   - **HOOK emotion** (0:00-0:15): What emotion opens the story?
   - **ACT 1-2 journey** (0:15-6:00): What experiences unfold?
   - **ACT 3 peak** (6:00-8:00): What's the emotional climax/revelation?
   - **Transformation**: How did Lilia's perspective change?

3. **Key Story Elements:**
   - Surprises or unexpected moments
   - Emotional peaks (awe, wonder, connection, reflection)
   - Challenges or struggles
   - Budget/practical details if prominent
   - Unique aspects that stand out
   - Expectation vs reality moments

4. **Story Type Identification:**
   - Expectation flip (thought X, but actually Y)
   - Discovery journey (found something unexpected)
   - Emotional transformation (changed perspective)
   - Challenge/experience (tried something new)
   - Cultural immersion (lived like local)
   - Budget exploration (what you get for $X)
   - Mystery/curiosity (stumbled upon something)

**Example Analysis Output:**

```
SCRIPT: dist/georgia/gonio-fortress/2025-11-04/script.md

PLACE: Gonio Fortress, Georgia
EMOTIONAL ARC: Skepticism → Surprise → Deep Connection → Awe
TRANSFORMATION: From dismissive ("just old stones") to deeply moved (feeling 2000 years of history)
KEY MOMENTS:
- Initial skepticism about visiting "another fortress"
- Physical connection (touching ancient stones)
- Unexpected emotional impact
- Realization about tangible history
STORY TYPE: Expectation vs Reality + Emotional Transformation
```

---

### STEP 3: Recommend Formula Categories

Based on the story analysis, identify the **2-3 formula categories** that best match the narrative.

**Matching Logic:**

| Story Type | Recommended Categories |
|------------|----------------------|
| Expectation flip, surprising transformation | 1. Expectation vs Reality<br>2. Story & Emotion<br>3. Mystery & Curiosity |
| Budget focus, cost transparency | 1. Budget & Lifestyle Hooks<br>2. Numbers & Lists<br>3. Challenge & Emotion |
| Discovery, hidden gems | 1. Mystery & Curiosity<br>2. Numbers & Lists<br>3. Social Proof & Trend |
| Challenge, personal experience | 1. Challenge & Emotion<br>2. Story & Emotion<br>3. Expectation vs Reality |
| Cultural immersion | 1. Challenge & Emotion<br>2. Story & Emotion<br>3. Before You Go & Practical |
| Shocking, controversial | 1. Shock & Controversy<br>2. Mystery & Curiosity<br>3. Expectation vs Reality |
| Trending, social proof | 1. Social Proof & Trend<br>2. Mystery & Curiosity<br>3. Numbers & Lists |
| Practical guide | 1. Before You Go & Practical<br>2. Numbers & Lists<br>3. Budget & Lifestyle |

**Output the recommendation:**

```markdown
### RECOMMENDED FORMULA CATEGORIES

Based on the emotional arc (Skepticism → Awe) and expectation-flip narrative:

**Primary Categories (generate 8-12 titles):**
1. **Expectation vs Reality** - Perfect match for "thought X but Y" transformation
2. **Story & Emotion** - Captures the deep emotional connection moment
3. **Mystery & Curiosity** - Honors the unexpected discovery element

**Secondary Categories (generate 5-8 titles):**
4. Numbers & Lists - For structured, practical angle
5. Social Proof & Trend - "Hidden gem" positioning
6. Challenge & Emotion - Personal experience angle
```

---

### STEP 4: Generate 15-20 Titles

**Title Generation Rules:**

1. **Distribution:**
   - 8-12 titles from PRIMARY categories
   - 5-8 titles from SECONDARY categories
   - Aim for 15-20 total titles

2. **Adaptation Requirements:**
   - Replace placeholder `___` with specific place name
   - Match formula emotion to script emotion
   - Maintain Lilia's authentic voice (raw, honest, conversational)
   - Keep titles under 80 characters for YouTube optimization
   - Be specific (use actual place names, not generic terms)

3. **Quality Standards:**
   - Must sound like something Lilia would actually say
   - Must reflect actual story content (no fake promises)
   - Balance curiosity with authenticity
   - Avoid excessive caps or manipulation tactics
   - Personal, first-person perspective preferred

**Example Title Generation:**

```
Formula: "I Thought ___ Was Overrated. I Was Wrong."
Script Insight: Lilia was skeptical about visiting another fortress
Generated Title: "I Thought Gonio Fortress Was Just Old Stones. I Was Wrong."
Rationale: Direct adaptation, captures exact transformation, authentic voice
```

---

### STEP 5: Rate Each Title

For each generated title, calculate a **Fit Score (1-10)** using the rating guide criteria:

**Rating Formula:**
```
Fit Score = (Authenticity × 0.35) + (Emotional Alignment × 0.35) + (CTR Potential × 0.30)
```

**Quick Rating Process:**

1. **Authenticity (×0.35):** Does it sound like Lilia? (1-10)
2. **Emotional Alignment (×0.35):** Does it match the script's arc? (1-10)
3. **CTR Potential (×0.30):** Does it create curiosity? (1-10)
4. **Calculate:** Add weighted scores, round to one decimal

**Example:**

```
Title: "I Thought Gonio Fortress Was Just Old Stones. I Was Wrong."

Authenticity: 9/10 (perfect Lilia voice - skepticism to wonder)
Emotional Alignment: 10/10 (exact script transformation)
CTR Potential: 8/10 (strong open loop, specific)

Fit Score: (9 × 0.35) + (10 × 0.35) + (8 × 0.30) = 9.05 → 9.1/10
```

---

### STEP 6: Rank and Sort Titles

1. **Sort all titles by Fit Score** (highest to lowest)
2. **Identify Top 5** (scores 8.5+) - these are the recommended titles
3. **Group remaining by category** for easy browsing
4. **Add rationale** for each title's score

---

### STEP 7: Generate Output Report

**CRITICAL: Output file structure is mandatory**

Save the markdown report to:
```
dist/[country]/[place]/[date]/titles-report.md
```

**File path rules:**
- `[country]`: Lowercase country name, use hyphens for spaces (e.g., "georgia", "united-states")
- `[place]`: Lowercase place name, use hyphens for spaces (e.g., "gonio-fortress", "old-town")
- `[date]`: Date in YYYY-MM-DD format (e.g., "2025-11-04")
- Filename: Always `titles-report.md`

**Example paths:**
- `dist/georgia/gonio-fortress/2025-11-04/titles-report.md`
- `dist/vietnam/hanoi-old-quarter/2025-11-06/titles-report.md`
- `dist/turkey/istanbul-grand-bazaar/2025-11-10/titles-report.md`

**Create directory if needed:**
```bash
mkdir -p dist/[country]/[place]/[date]
```

---

## Output Format: titles-report.md

```markdown
# YouTube Title Options: [Place Name]

**Generated:** [Date and Time]
**Script:** [Path to script file]
**Total Titles Generated:** [Number]

---

## 📊 Story Analysis Summary

**Place:** [Place Name, Country]
**Emotional Arc:** [Start Emotion] → [End Emotion]
**Story Type:** [Type(s)]
**Key Transformation:** [Brief description]

**Recommended Formula Categories:**
1. [Category 1] - [Why it fits]
2. [Category 2] - [Why it fits]
3. [Category 3] - [Why it fits]

---

## 🏆 TOP 5 RECOMMENDED TITLES

### 1. [Title]
- **Formula:** [Category - Specific Formula]
- **Fit Score:** [X.X/10]
- **Rationale:**
  - Authenticity ([score]/10): [Brief explanation]
  - Emotional Alignment ([score]/10): [Brief explanation]
  - CTR Potential ([score]/10): [Brief explanation]

[Repeat for titles 2-5]

---

## 📝 ALL TITLES BY CATEGORY

### Category 1: [Category Name]

**[Rank]. [Title]** — Fit Score: [X.X/10]
- **Formula:** [Formula used]
- **Rationale:** [One-line explanation]

[Repeat for all titles in this category]

### Category 2: [Category Name]

[Continue for all categories]

---

## 💡 Usage Notes

**How to choose:**
- Top 5 are ready to use immediately
- Consider A/B testing top 3 titles
- Match title emotion to thumbnail mood
- Shorter titles (under 60 chars) work better on mobile

**Next steps:**
- Choose 1-2 favorites for A/B testing
- Create thumbnails that match title emotion
- Track CTR performance in `references/title-formulas.md`
- Update formula notes based on performance

---

**Generated by:** Travel Title Generator Skill
**Formula Bank:** 100 proven travel video title formulas
```

---

## Key Principles

### 1. Authenticity Over Clickbait
- Lilia's voice is raw, honest, and conversational
- Titles must reflect actual story content
- Avoid manipulative tactics or false promises
- Balance curiosity with integrity

### 2. Emotion-First Matching
- The script's emotional arc is the north star
- Match title emotion to ACT 3 peak emotion
- Transformation stories need transformation titles
- Don't force mismatched formulas

### 3. Specificity Creates Curiosity
- Use actual place names, not generic terms
- Specific details are more intriguing than vague promises
- "Gonio Fortress" > "a fortress in Georgia"
- "I thought X, but Y" > "This place surprised me"

### 4. Strategic Category Selection
- Not all formulas fit all stories
- Primary categories (8-12 titles) must align with narrative
- Secondary categories (5-8 titles) provide variety
- Don't generate titles from mismatched categories

### 5. Rating Must Be Honest
- Spread scores across the full 1-10 range
- Not all titles should score 8+
- Clear winners (9-10) and clear losers (1-4)
- Rating is about fit, not personal preference

---

## Quality Checklist

Before delivering the report, verify:

### ✓ Analysis Complete
- [ ] Script fully read and analyzed
- [ ] Emotional arc clearly identified
- [ ] Story type determined
- [ ] Key transformation noted

### ✓ Category Matching
- [ ] 2-3 primary categories recommended
- [ ] Categories match story type
- [ ] Rationale provided for each category
- [ ] 8-12 titles from primary, 5-8 from secondary

### ✓ Title Generation
- [ ] 15-20 titles total generated
- [ ] All titles use specific place names
- [ ] Titles under 80 characters
- [ ] Authentic to Lilia's voice
- [ ] Match actual story content

### ✓ Rating & Ranking
- [ ] All titles rated with fit scores
- [ ] Scores calculated correctly (3 criteria × weights)
- [ ] Titles sorted by score (highest first)
- [ ] Top 5 clearly identified
- [ ] Rationale provided for each score

### ✓ Output Format
- [ ] File saved to correct path: `dist/[country]/[place]/[date]/titles-report.md`
- [ ] All required sections included
- [ ] Markdown formatting correct
- [ ] Story analysis summary at top
- [ ] Top 5 section complete
- [ ] All titles organized by category

---

## Common Use Cases

### Use Case 1: Generate Titles for New Script
```
User: "Generate titles for dist/georgia/gonio-fortress/2025-11-04/script.md"
```
**Action:**
1. Load references
2. Read script
3. Analyze emotional arc (skepticism → awe)
4. Recommend: Expectation vs Reality, Story & Emotion, Mystery & Curiosity
5. Generate 15-20 titles
6. Rate and rank
7. Output to `dist/georgia/gonio-fortress/2025-11-04/titles-report.md`

### Use Case 2: A/B Test Variants
```
User: "I need A/B test titles for the Hanoi Old Quarter video"
```
**Action:**
1. Load references
2. Read script at `dist/vietnam/hanoi-old-quarter/[date]/script.md`
3. Focus on Top 5 highest-scoring titles
4. Generate 2-3 slight variations of each top title
5. Output report with A/B testing recommendations

### Use Case 3: Category-Specific Request
```
User: "Give me budget-focused titles for this script"
```
**Action:**
1. Load references
2. Read script
3. Focus on Budget & Lifestyle Hooks category
4. Generate 10-15 titles from budget formulas
5. Rate and output

### Use Case 4: Regenerate with Different Focus
```
User: "These titles are too clickbaity, make them more authentic"
```
**Action:**
1. Review previous titles
2. Prioritize Authenticity weight (increase to 50%)
3. Focus on Story & Emotion and Challenge & Emotion categories
4. Regenerate with authenticity emphasis
5. Output new report

---

## Best Practices

### Do:
✓ **Always read the full script** before generating titles
✓ **Match emotion precisely** - use the script's actual transformation
✓ **Use specific place names** in every title
✓ **Spread scores honestly** - not everything is 8+
✓ **Prioritize authenticity** - Lilia's voice over pure CTR
✓ **Generate variety** - cover multiple categories
✓ **Provide clear rationale** for each score
✓ **Keep titles under 80 characters** for YouTube optimization

### Don't:
✗ **Generate generic titles** that could apply to any place
✗ **Force mismatched formulas** (e.g., budget titles for emotional stories)
✗ **Use fake hype** or manipulative language
✗ **Promise what the script doesn't deliver**
✗ **Give all titles similar scores** (spread them out!)
✗ **Skip the analysis step** (it's critical for matching)
✗ **Use excessive caps or punctuation** (!!!, ALL CAPS)
✗ **Create clickbait** that betrays Lilia's authentic voice

---

## Resources

### Available References
1. **title-formulas.md** - 100 proven formulas organized by 9 categories
2. **title-rating-guide.md** - Detailed scoring criteria and examples

### Formula Categories
1. Expectation vs Reality (Emotional Flip)
2. Numbers & Lists (Structured Curiosity)
3. Mystery & Curiosity (Open Loop)
4. Challenge & Emotion (First-Person Experience)
5. Social Proof & Trend Hooks
6. Story & Emotion (Narrative Titles)
7. Shock & Controversy
8. Before You Go & Practical Hooks
9. Budget & Lifestyle Hooks

---

## Remember: The Goal

Create titles that:
1. **Sound like Lilia** - authentic, raw, conversational
2. **Match the story** - reflect actual emotional arc
3. **Create curiosity** - open loops without manipulation
4. **Stand out** - specific, unique, intriguing
5. **Drive clicks** - proven formulas optimized for CTR

**The best titles make people click because they promise an authentic, emotional journey - not because they're manipulative.**

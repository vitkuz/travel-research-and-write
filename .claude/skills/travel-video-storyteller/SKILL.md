---
name: travel-video-storyteller
description: Transform travel research into compelling video narratives. Use when users need to create travel video scripts, structure vlog content, develop story arcs for destination content, or convert research/data about travel experiences into engaging video stories. Provides narrative frameworks, hooks, pacing guidelines, script templates, and analysis tools for YouTube/Instagram/TikTok travel content.
license: Complete terms in LICENSE.txt
---

# Travel Video Storyteller

Transform travel research (destinations, experiences, insights, data) into compelling video narratives for YouTube, Instagram, TikTok, and other platforms.

## When to Use This Skill

Trigger this skill when users want to:
- Create video scripts from travel research
- Structure travel vlog content
- Develop story arcs for destination videos
- Convert research data into engaging narratives
- Generate hooks and openings for travel content
- Plan video pacing and timing
- Analyze travel experiences for story-worthy elements

## Core Capabilities

1. **Narrative Structure Selection** - Choose from 7 proven story frameworks (Hero's Journey, Day-in-Life, Comparison, Discovery Arc, Hidden Gems, Budget Challenge, Time-Lapse)
2. **Hook Generation** - Create attention-grabbing openings using 10 tested patterns
3. **Research Analysis** - Extract story elements from raw travel data
4. **Script Development** - Generate complete video scripts with timing and shot lists
5. **Pacing Optimization** - Apply platform-specific pacing guidelines

## Workflow

### Step 1: Understand the Content

**Gather information**:
- What travel research/experiences do they have?
- What platform(s) is this for? (YouTube/Instagram/TikTok)
- What's the target video length?
- What's their style? (Cinematic/vlog/educational)
- What's the core message or transformation?

**Key questions to ask**:
- "What's the one thing viewers should remember from this video?"
- "What surprised you most about this experience?"
- "What went wrong or challenged you?"
- "Who did you meet that impacted the journey?"

### Step 2: Select Narrative Structure

**Load the narrative structures reference**:
```
view references/narrative-structures.md
```

**Choose based on content type**:
- **Epic/transformative journey** → Hero's Journey
- **Single day exploration** → Day-in-Life
- **Two options/approaches** → Comparison Journey
- **First-time experience** → Discovery Arc
- **Compilation of spots** → Hidden Gems (Curator's Guide)
- **Travel on budget** → Budget Challenge
- **Quick city guide** → Time-Lapse Journey

**Consider combining structures** for complex narratives.

### Step 3: Transform Research into Story

**Load the research-to-story guide**:
```
view references/research-to-story.md
```

**Apply the five-step transformation**:
1. Identify story-worthy elements (contradictions, emotions, stakes)
2. Find the through-line (what's this REALLY about?)
3. Construct cause-and-effect chains
4. Add human elements (people, reactions, dialogue)
5. Structure with intentional gaps (foreshadowing, delayed payoff)

**Use the "So What?" test** - Every piece of research must answer: "So what? Why does this matter?"

### Step 4: Generate Hooks

**Load the hooks reference**:
```
view references/hooks-openings.md
```

**Select hook pattern(s)**:
- Bold Claim - "[Superlative] + [Place] + [Unexpected Element]"
- Contradiction - "Everyone says [X], but [Opposite Reality]"
- Question Hook - "[Provocative Question] + [Visual Proof]"
- Time Crunch - "I have [Limited Time] to [Ambitious Goal]"
- Personal Stakes - "[Personal Challenge/Fear] + [Forced to Face It]"
- What They Don't Show - "The truth about [Popular Destination]"
- Curiosity Gap - Show something bizarre without explaining
- Price Drop - "[Expensive Thing] for [Shockingly Cheap Price]"
- Countdown - "[Number] [Things] that [Strong Claim]"
- Local Secret - "A [Local] told me about [Hidden Thing]"

**Create 3-5 hook options** and select the strongest.

### Step 5: Develop the Script

**Load the script template**:
```
view assets/script-template.md
```

**Use the template structure**:
1. **Hook** (0:00-0:10) - Grab attention immediately
2. **Act 1: Setup** (0:10-2:00) - Context, stakes, first impression
3. **Act 2: Journey** (2:00-8:00) - Multiple beats with varied pacing
4. **Act 3: Climax** (8:00-9:30) - Peak emotional moment
5. **Outro** (9:30-10:00) - Reflection and call-to-action

**Fill in each section** with:
- Visual descriptions (wide/medium/close-up)
- Audio (dialogue/narration)
- B-roll shot lists
- Music cues
- Pacing notes

### Step 7: Compleate audio script for the hall video

### Step 8: Optimize Pacing

**Load the pacing guide**:
```
view references/pacing-timing.md
```

**Apply platform-specific timing**:
- **YouTube**: 6-8 min (ideal), 10-13 min (mid-form), 15-20+ min (long-form)
- **Instagram/TikTok**: 15-30 sec (quick tip), 45-60 sec (mini-story), 2-3 min (max)

**Use pace cycles** (prevent monotony):
1. Fast segment (60s): Action, exploration
2. Slow segment (30s): Reflection, single moment
3. Medium segment (45s): Information, story
4. Repeat with variation

**Apply the 10-second rule**: Every 10 seconds, deliver new information, visual change, emotional beat, or story progression.

### Step 9: Optional - Analyze Research Data

If the user has structured travel research data (JSON format), use the story analyzer script:

```bash
python scripts/story_analyzer.py input.json --format markdown
```

**Input format example**:
```json
{
  "destination": "Bangkok, Thailand",
  "expectations": ["touristy", "expensive", "crowded"],
  "reality": ["authentic pockets exist", "incredibly affordable", "locals are welcoming"],
  "unique_facts": [
    "Street market operating since 1982",
    "40+ family-run food vendors",
    "Locals outnumber tourists 10:1"
  ],
  "challenges": [
    "Language barrier at first",
    "Getting lost in alleyways",
    "Finding authentic spots"
  ],
  "surprises": [
    "Grandmother invited me to share table",
    "Vendor taught me Thai phrases",
    "Found hidden rooftop garden"
  ],
  "learnings": [
    "Best travel moments can't be planned",
    "Locals want to share their culture",
    "Getting lost leads to best discoveries"
  ],
  "experiences": [
    "Morning market at 6am",
    "Cooking class with local family",
    "Evening tuk-tuk ride through old town"
  ],
  "locations": [
    "Khlong Toei Market",
    "Pak Khlong Talat (flower market)",
    "Wang Lang Market"
  ]
}
```

**The script outputs**:
- Recommended narrative structure
- Top hook options with emotional/visual ratings
- Organized story beats (setup, journey, climax)
- Key insights and visual moments
- Estimated video duration

## Key Principles

### 1. Story Over Information
Research tells WHAT happened. Story shows WHY it mattered.
- Facts need emotional context
- Every element must serve the through-line
- Functional information without meaning is just data

### 2. Front-Load Value
Viewers decide in 3 seconds whether to stay.
- Hook must be visual AND verbal
- Don't save the best for last
- First 30 seconds = setup complete

### 3. Cause and Effect
Random events don't create investment.
- Each beat should lead to the next
- Payoffs must be earned with setups
- Show how A caused B, which led to C

### 4. Human Connection
Places are settings. People are stories.
- Include personal vulnerability
- Show at least one meaningful interaction
- Express relatable emotions
- Internal transformation evident

### 5. Intentional Pacing
Consistent pace = monotony.
- Vary pace deliberately (fast/slow/medium cycles)
- Match pace to content energy
- Use breathers after intense moments
- Every 10 seconds = something new

## Output Formats

### Full Video Script
Use `assets/script-template.md` structure - includes:
- Hook and opening (0-30s)
- Three-act structure with timing
- Shot-by-shot descriptions
- Audio/music cues
- B-roll lists
- Post-production notes

### Story Structure Analysis
Use `scripts/story_analyzer.py` - generates:
- Recommended narrative framework
- Hook options with ratings
- Organized story beats
- Visual moments
- Key insights

### Quick Hook Options
Generate 3-5 hooks using patterns from `references/hooks-openings.md` - include:
- Pattern type (bold claim, contradiction, etc.)
- Example hook text
- Visual description
- Why it works

### Narrative Outline
High-level structure based on `references/narrative-structures.md` - include:
- Structure choice (Hero's Journey, Discovery Arc, etc.)
- Beat-by-beat breakdown
- Timing estimates
- Emotional arc
- Key moments to capture

## Common Use Cases

### Use Case 1: Research to Script
**Input**: Travel research notes, photos, experiences
**Process**: 
1. Load research-to-story transformation guide
2. Extract story-worthy elements
3. Choose narrative structure
4. Generate hooks
5. Develop full script with template

**Output**: Complete video script ready for filming/editing

### Use Case 2: Improve Existing Content
**Input**: Existing vlog or rough cut
**Process**:
1. Identify weak spots (no hook, slow middle, weak ending)
2. Apply pacing guidelines
3. Suggest structural improvements
4. Generate stronger hooks
5. Recommend cuts/additions

**Output**: Edit recommendations with specific timing

### Use Case 3: Multi-Platform Adaptation
**Input**: Long-form YouTube video
**Process**:
1. Identify platform-specific requirements
2. Extract strongest 60-second segment for Instagram/TikTok
3. Create separate hooks for each platform
4. Adjust pacing for shorter attention spans

**Output**: Platform-optimized versions of same content

### Use Case 4: Travel Compilation Video
**Input**: Multiple destination experiences
**Process**:
1. Choose Hidden Gems or Countdown structure
2. Rank experiences by visual/emotional impact
3. Create throughline connecting all gems
4. Design transitions between locations

**Output**: Cohesive compilation with narrative thread

## Best Practices

### Do:
✓ Start with the core message/transformation
✓ Choose structure before writing
✓ Test hooks with "would I click?" honesty
✓ Apply "so what?" test to all research
✓ Vary pacing intentionally
✓ Include personal vulnerability
✓ Front-load value (don't save best for last)
✓ Show cause-and-effect chains
✓ Let important moments breathe (20-40s)
✓ End with transformation, not facts

### Don't:
✗ Include every location/fact/experience
✗ Start with "hey guys, welcome back"
✗ Maintain consistent pace throughout
✗ Make it about the destination alone
✗ Skip the human element
✗ Save climax for final minute
✗ Forget the "why it mattered"
✗ Use generic openings ("in this video I'll show you...")
✗ End with "thanks for watching"
✗ Announce what you'll do (just do it)

## Skill Resources

### References (load as needed)
- **narrative-structures.md** - 7 proven story frameworks with timing/structure
- **hooks-openings.md** - 10 hook patterns with examples
- **pacing-timing.md** - Platform-specific pacing, shot duration, rhythm
- **research-to-story.md** - 5-step transformation process

### Assets
- **script-template.md** - Complete video script template with timing

### Scripts
- **story_analyzer.py** - Analyze JSON research data, extract story elements

## Tips for Different Styles

### Cinematic/Documentary Style
- Use Hero's Journey or Discovery Arc
- Longer shots (4-6 seconds)
- Voiceover-driven
- Dramatic music cues
- Let visuals lead

### Vlog Style (Casual)
- Day-in-Life or Time-Lapse structures
- Start mid-action
- Conversational tone
- Authentic reactions
- Faster cuts (2-4 seconds)

### Educational/Informative
- Hidden Gems or Comparison structures
- Lead with the insight
- Show proof immediately
- Balance information with story
- Clear takeaways

### Budget/Challenge Content
- Budget Challenge or Comparison structures
- Show real prices/receipts
- Honest struggles and wins
- Practical tips embedded in story
- Relatable resource constraints

## Platform-Specific Guidance

### YouTube (Primary)
- 6-8 minutes = algorithm sweet spot
- Can have breathing room
- Longer buildups work if earned
- Ad breaks at natural transitions

### Instagram Reels/TikTok
- First second is EVERYTHING
- Maximum 60 seconds for engagement
- One clear arc/point
- Text overlays for key info
- Audio-off test essential

### YouTube Shorts
- 15-30 seconds ideal
- Single compelling moment
- No complex narratives
- Hook = entire video
- Vertical format

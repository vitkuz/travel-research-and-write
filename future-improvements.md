# Analysis of Your Claude Code Setup: Skills, Agents & Slash Commands

## Current Setup Overview

Your project is a **travel content creation pipeline** focused on transforming destination research into compelling video narratives with Lilia's authentic voice. Here's what you have:

### **Skills (5 total)**
1. **travel-video-storyteller** - Transforms research into video scripts with narrative structures
2. **travel-title-generator** - Generates 15-20 ranked YouTube titles using 100 formulas
3. **destination-research** - Compiles top 10 places (managed skill)
4. **place-research** - Deep research on specific places (managed skill)
5. **social-media-adapter** - Converts scripts to Twitter threads, Instagram carousels/captions

### **Agents (4 total)**
1. **destination-guide-pipeline** - Orchestrator agent (delegates to other agents)
2. **place-finder** - Finds 10 must-visit places for a destination
3. **place-researcher** - Researches specific places in detail
4. **story-writer** - Transforms research into voiceover scripts

### **Slash Commands**
Currently: **None** (no `.claude/commands/` directory)

---

## New Ideas for Skills, Agents & Slash Commands

Based on your workflow and the Claude Code documentation, here are strategic additions:

### **🎯 New Skills to Build**

#### 1. **thumbnail-designer**
```yaml
name: thumbnail-designer
description: Generate thumbnail concepts and text overlay recommendations for travel videos. Use when users need thumbnail ideas, A/B test variants, or visual branding for YouTube videos.
```
**Why:** You generate titles and scripts, but thumbnails are critical for CTR. This skill would:
- Analyze script emotional peaks for thumbnail moments
- Suggest text overlays matching title emotion
- Provide color palette from brand/destination
- Generate 3-5 A/B test concepts

**Workflow:** Read script → Identify visual peak moments → Match to title emotion → Generate design specs (Canva-ready)

---

#### 2. **hashtag-strategist**
```yaml
name: hashtag-strategist
description: Generate platform-specific hashtag strategies for travel content. Use when users need Instagram hashtags, TikTok tags, or YouTube keywords optimized for reach and discoverability.
```
**Why:** Social media adapter creates captions but doesn't deeply optimize hashtags. This skill would:
- Research trending hashtags by destination/theme
- Balance broad reach vs. niche community tags
- Provide rotation strategy (avoid repetition)
- Track hashtag performance over time

---

#### 3. **voiceover-timer**
```yaml
name: voiceover-timer
description: Calculate precise voiceover timing and pacing from scripts. Use when users need to sync narration to video edits, identify cuts, or optimize pacing for platform length constraints.
```
**Why:** Scripts have timing markers but no word-count-to-duration calculator. This skill would:
- Calculate reading time (150-160 WPM for narration)
- Identify sections that exceed platform limits
- Suggest cuts without losing narrative flow
- Export timing cues for video editors (Premiere, DaVinci)

---

#### 4. **seo-optimizer**
```yaml
name: seo-optimizer
description: Optimize YouTube descriptions, tags, and metadata for SEO and discoverability. Use when users need video descriptions, keyword strategies, or chapter timestamps for travel content.
```
**Why:** You have titles but no description/metadata generation. This skill would:
- Generate YouTube descriptions (first 150 chars optimized)
- Extract keywords from script for tags
- Create chapter timestamps from script acts
- Suggest related video links for cards/end screens

---

#### 5. **engagement-analyzer**
```yaml
name: engagement-analyzer
description: Analyze performance metrics and suggest content improvements. Use when users have analytics data from YouTube, Instagram, or Twitter and want data-driven recommendations.
```
**Why:** You create content but don't close the loop with performance analysis. This skill would:
- Parse analytics exports (CSV/JSON)
- Identify high-performing content patterns
- Suggest title/hook formulas that work best
- Recommend content topics based on engagement

---

### **🤖 New Agents to Build**

#### 6. **video-editor-assistant**
```yaml
name: video-editor-assistant
description: Use when users need shot lists, b-roll recommendations, or editing notes from scripts. Generates Premiere/DaVinci-compatible editing instructions.
```
**Why:** Scripts have narrative but limited production guidance. This agent would:
- Parse script for shot types (wide/medium/close-up)
- Generate b-roll shopping lists by timestamp
- Create editing notes (cuts, transitions, music cues)
- Export timeline markers for NLEs

---

#### 7. **fact-checker**
```yaml
name: fact-checker
description: Use when users need to verify historical facts, dates, or claims in travel content. Searches authoritative sources and flags potential inaccuracies.
```
**Why:** Travel content includes historical/cultural facts. This agent would:
- Extract factual claims from scripts/research
- Cross-reference with Wikipedia, travel authorities
- Flag unverified claims with confidence scores
- Suggest corrections or disclaimers

---

#### 8. **competitor-analyzer**
```yaml
name: competitor-analyzer
description: Use when users want to analyze competitor content, identify gaps, or benchmark their content strategy against top travel creators.
```
**Why:** Content strategy needs competitive intelligence. This agent would:
- Analyze top-performing videos in a niche
- Extract title/thumbnail patterns
- Identify underserved topics/destinations
- Suggest differentiation strategies

---

#### 9. **batch-content-generator**
```yaml
name: batch-content-generator
description: Use when users want to generate multiple stories in parallel for a destination or theme. Orchestrates research → script → titles → social media for 5-10 places simultaneously.
```
**Why:** `destination-guide-pipeline` handles one destination, but you might want themed batches. This agent would:
- Accept list of places (e.g., "Top 10 Georgia Fortresses")
- Run place-researcher + story-writer + title-generator in parallel
- Generate consistent narrative style across batch
- Output organized reports

---

### **⚡️ Slash Commands to Build**

#### 10. **/story** - Quick Story Generator
```markdown
---
description: Generate a complete travel story from place name
argument-hint: [place-name]
allowed-tools: Task, Read, Write
---

Generate a complete travel video story for: $1

Pipeline:
1. Research place details
2. Write script in Lilia's voice
3. Generate 15-20 title options
4. Create social media adaptations
5. Output all files to dist/[country]/[place]/[date]/
```
**Usage:** `/story "Hagia Sophia"`

---

#### 11. **/titles** - Quick Title Generation
```markdown
---
description: Generate YouTube titles from script file
argument-hint: [script-path]
---

Generate YouTube titles for script at: $ARGUMENTS

Use travel-title-generator skill to:
- Analyze emotional arc
- Generate 15-20 ranked titles
- Output to titles-report.md
```
**Usage:** `/titles dist/georgia/gonio-fortress/2025-11-04/script.md`

---

#### 12. **/social** - Quick Social Media Breakdown
```markdown
---
description: Convert script to social media content
argument-hint: [script-path]
---

Transform script to social media content: $ARGUMENTS

Use social-media-adapter skill to:
- Generate Twitter thread (5-10 tweets)
- Create Instagram carousel (10 slides)
- Write Instagram caption
- Output strategy document
```
**Usage:** `/social dist/georgia/gonio-fortress/2025-11-04/script.md`

---

#### 13. **/publish** - Publishing Checklist
```markdown
---
description: Generate pre-publish checklist for content
argument-hint: [place-folder-path]
---

Create publishing checklist for: $ARGUMENTS

Verify:
- [ ] Script exists and follows template
- [ ] Titles generated and ranked
- [ ] Social media content created
- [ ] Thumbnail concepts ready
- [ ] SEO metadata prepared
- [ ] All files in correct directory structure
```
**Usage:** `/publish dist/georgia/gonio-fortress/2025-11-04/`

---

#### 14. **/batch** - Batch Process Places
```markdown
---
description: Process multiple places in parallel
argument-hint: [places-json-path]
---

Batch process all places in: $ARGUMENTS

For each place in JSON:
1. Research place (@agent-place-researcher)
2. Write story (@agent-story-writer)
3. Generate titles (travel-title-generator)
4. Create social media (social-media-adapter)

Run all in parallel for maximum speed.
```
**Usage:** `/batch dist/georgia/places.json`

---

#### 15. **/analyze** - Content Performance Analysis
```markdown
---
description: Analyze content performance from analytics
argument-hint: [analytics-csv-path]
---

Analyze performance data from: $ARGUMENTS

Use engagement-analyzer skill to:
- Parse analytics CSV/JSON
- Identify top-performing patterns
- Suggest content improvements
- Output recommendations report
```
**Usage:** `/analyze analytics/youtube-2025-10.csv`

---

## Strategic Recommendations

### **Immediate Priorities (Build First)**

1. **thumbnail-designer skill** - Closes CTR optimization gap (title + thumbnail)
2. **seo-optimizer skill** - YouTube descriptions/metadata missing from pipeline
3. **/story slash command** - Single command to run entire pipeline (huge UX win)
4. **/social slash command** - Quick way to repurpose existing scripts

### **Medium-Term Additions**

5. **voiceover-timer skill** - Solves practical production problem
6. **video-editor-assistant agent** - Bridges script → editing workflow
7. **/batch slash command** - Scale content production efficiently

### **Long-Term Enhancements**

8. **engagement-analyzer skill** - Close the feedback loop
9. **competitor-analyzer agent** - Strategic content planning
10. **fact-checker agent** - Quality assurance

---

## Implementation Tips

### **For Skills:**
- Keep `SKILL.md` descriptions specific (trigger phrases matter)
- Use `references/` subfolder for large guides
- Include persona reference loads where Lilia's voice is needed
- Add quality checklists at the end

### **For Agents:**
- Use agents for multi-step autonomous workflows
- Orchestrator agents (like `destination-guide-pipeline`) are powerful
- Specify `model: haiku` for cost-effective simple tasks
- Add color coding for visual organization

### **For Slash Commands:**
- Store in `.claude/commands/` (project-level) for team sharing
- Use `$1`, `$2` for positional args or `$ARGUMENTS` for all
- Add `argument-hint` for autocomplete UX
- Use `allowed-tools` to restrict permissions
- Can execute bash with `!`backticks for pre-command info

---

## Bonus: Plugin Idea

**"Travel Content Studio" Plugin** - Package your best skills/agents/commands:
```
.claude/
└─ plugins/
   └─ travel-content-studio/
      ├─ skills/
      │  ├─ travel-video-storyteller/
      │  ├─ travel-title-generator/
      │  ├─ social-media-adapter/
      │  ├─ thumbnail-designer/
      │  └─ seo-optimizer/
      ├─ agents/
      │  ├─ destination-guide-pipeline.md
      │  └─ video-editor-assistant.md
      └─ commands/
         ├─ story.md
         ├─ social.md
         └─ batch.md
```

Share with the Claude Code community or use across your projects!

---

## Claude Code Documentation Summary

### **What Are Skills?**
Skills are "modular capabilities that extend Claude's functionality through organized folders containing instructions, scripts, and resources." Unlike slash commands that you explicitly trigger, skills are **model-invoked**—Claude autonomously decides when to activate them based on your request and the skill's description.

**Storage:**
- **Personal Skills** (`~/.claude/skills/`): Available across all projects
- **Project Skills** (`.claude/skills/`): Shared with team via git

**Key Requirements:**
- `SKILL.md` file with YAML frontmatter (name, description)
- Description is critical for discovery (include what it does AND when to use it)
- Optional: `allowed-tools` to restrict capabilities
- Supporting files in same directory (references/, assets/, scripts/)

---

### **What Are Subagents?**
Subagents are specialized AI assistants that Claude Code delegates work to. Each operates independently with its own context window, custom system prompt, and configurable tool access.

**Key Advantages:**
- **Context Management**: Separate context prevents main conversation clutter
- **Specialized Performance**: Tailored configurations for domain expertise
- **Reusability**: Use across projects and share with team
- **Granular Permissions**: Control tool access per agent

**Storage:**
- **Project-level** (`.claude/agents/`): Highest priority, project-specific
- **User-level** (`~/.claude/agents/`): Lower priority, available everywhere

**Configuration:**
```yaml
---
name: unique-identifier
description: When and why to use this subagent
tools: Tool1, Tool2  # Optional
model: sonnet  # Optional (or haiku, opus)
color: yellow  # Optional visual coding
---

System prompt with detailed instructions...
```

**Usage:**
- **Automatic**: Claude analyzes tasks and invokes appropriate agents
- **Explicit**: "Use the debugger subagent to investigate this error"
- **Chaining**: Combine multiple agents for complex workflows

---

### **What Are Slash Commands?**
Custom slash commands let you define reusable prompts as Markdown files that Claude Code can execute.

**Storage:**
- **Project Commands** (`.claude/commands/`): Shared with team (appear as "(project)")
- **Personal Commands** (`~/.claude/commands/`): Use across all projects (appear as "(user)")

**Syntax:**
```markdown
---
description: Brief command description
allowed-tools: Bash(git status:*), Read, Write
model: sonnet  # Optional
argument-hint: [expected-args]  # Shows in autocomplete
disable-model-invocation: false  # Optional
---

Your command prompt here.

Use $1, $2, $3 for positional arguments.
Use $ARGUMENTS for all arguments.

Execute bash: !`git status`
Reference files: @src/utils/helpers.js
```

**Features:**
- **Arguments**: Positional (`$1`, `$2`) or all (`$ARGUMENTS`)
- **Namespacing**: Organize in subdirectories (`.claude/commands/frontend/component.md` → `/component`)
- **Bash Execution**: Use `!`backticks to run shell commands before prompt
- **File References**: Use `@` prefix to include file contents

**Integration with Claude:**
- Add `description` frontmatter for SlashCommand tool invocation
- Claude can execute commands programmatically during conversations
- Reference in instructions: "Run /write-unit-test when starting to write tests"

---

### **Skills vs Slash Commands vs Agents**

| Feature | Skills | Slash Commands | Agents |
|---------|--------|----------------|--------|
| **Invocation** | Automatic (model-decided) | Explicit user command | Automatic or explicit |
| **Best For** | Reusable capabilities | Quick shortcuts | Multi-step autonomous workflows |
| **Context** | Main conversation | Main conversation | Separate context window |
| **Complexity** | Medium (instructions + assets) | Simple (prompt + args) | High (full system prompt) |
| **Tool Control** | Optional restrictions | Required allowed-tools | Optional restrictions |
| **Sharing** | Project or personal | Project or personal | Project or personal |

**General Guidance:**
- **Use Skills** when Claude should automatically recognize and apply a capability
- **Use Slash Commands** for frequently-used prompts you want to trigger manually
- **Use Agents** for complex, multi-step workflows that benefit from isolated context

---

## Quick Reference: File Structure

```
research-and-write/
├─ .claude/
│  ├─ skills/
│  │  ├─ travel-video-storyteller/
│  │  │  ├─ SKILL.md
│  │  │  ├─ references/
│  │  │  │  ├─ narrative-structures.md
│  │  │  │  ├─ hooks-openings.md
│  │  │  │  ├─ pacing-timing.md
│  │  │  │  ├─ elevenlabs-audio-tags.md
│  │  │  │  └─ persona-to-adopt-improved.md
│  │  │  └─ assets/
│  │  │     └─ script-template.md
│  │  ├─ travel-title-generator/
│  │  │  ├─ SKILL.md
│  │  │  └─ references/
│  │  │     ├─ title-formulas.md
│  │  │     └─ title-rating-guide.md
│  │  └─ social-media-adapter/
│  │     ├─ SKILL.md
│  │     └─ references/
│  │        └─ persona-to-adopt-improved.md
│  ├─ agents/
│  │  ├─ destination-guide-pipeline.md
│  │  ├─ place-finder.md
│  │  ├─ place-researcher.md
│  │  └─ story-writer.md
│  ├─ commands/  # TO BE CREATED
│  │  ├─ story.md
│  │  ├─ titles.md
│  │  ├─ social.md
│  │  ├─ publish.md
│  │  ├─ batch.md
│  │  └─ analyze.md
│  └─ settings.local.json
├─ dist/
│  ├─ georgia/
│  │  ├─ places.json
│  │  └─ [place-name]/
│  │     └─ [YYYY-MM-DD]/
│  │        ├─ script.md
│  │        ├─ titles-report.md
│  │        └─ social-media/
│  │           ├─ twitter-thread.md
│  │           ├─ instagram-carousel.md
│  │           ├─ instagram-caption.md
│  │           └─ content-strategy.md
│  └─ vietnam/
│     └─ [similar structure]
├─ Lilya_Persona_EN.md
├─ how-lily-talks.txt
└─ future-improvements.md  # THIS FILE
```

---

## Next Steps

1. **Review this document** and prioritize which additions align with your workflow
2. **Start with high-impact, low-effort items**: `/social` and `/titles` slash commands
3. **Build iteratively**: Create one skill/agent/command at a time, test thoroughly
4. **Document as you go**: Update persona references, add examples, track performance
5. **Share with community**: Package as plugin when mature

---

**Created:** 2025-11-07
**Last Updated:** 2025-11-07
**Version:** 1.0

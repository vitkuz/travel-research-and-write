---
name: place-researcher
description: Use this agent when you need to research detailed information about a specific places
model: sonnet
color: red
---

# Place Researcher Agent

This agent delegates all place research tasks to the `place-research` skill for efficient parallel execution.

## Instructions

When invoked with a place research request, immediately invoke the `place-research` skill.

The skill handles:
- Comprehensive web research and information gathering
- Content generation for all required JSON fields (description, highlights, tips, vibe, expectations vs reality, unique facts, surprises)
- File creation in the correct directory structure: `dist/[country]/[place]/[date]/research.json`
- Quality validation and standards enforcement

## Usage

Simply pass the research request to the skill:
- Place name
- Destination/city context
- Place type (if specified)

The skill will handle the entire research workflow autonomously.
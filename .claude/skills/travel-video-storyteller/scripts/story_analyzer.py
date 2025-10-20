#!/usr/bin/env python3
"""
Travel Research Story Analyzer

Analyzes travel research data (destinations, experiences, insights) and extracts
story elements suitable for video storytelling.

Usage:
    python story_analyzer.py input.json --output story_elements.json
    python story_analyzer.py input.json --format markdown
"""

import json
import sys
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from collections import defaultdict
import argparse


@dataclass
class StoryElement:
    """Represents a story element extracted from research"""
    element_type: str  # hook, conflict, climax, insight, etc.
    content: str
    emotional_weight: int  # 1-10 scale
    visual_potential: int  # 1-10 scale
    timestamp_estimate: str  # Where in video this might fit
    tags: List[str]


@dataclass
class StoryStructure:
    """Represents a complete story structure"""
    title: str
    structure_type: str
    duration_target: str
    hooks: List[StoryElement]
    setup_beats: List[StoryElement]
    journey_beats: List[StoryElement]
    climax: StoryElement
    insights: List[StoryElement]
    visual_moments: List[StoryElement]


class TravelResearchAnalyzer:
    """Analyzes travel research and extracts story-worthy elements"""
    
    def __init__(self, research_data: Dict[str, Any]):
        self.data = research_data
        self.story_elements = []
        
    def analyze(self) -> StoryStructure:
        """Main analysis method"""
        # Extract different types of story elements
        hooks = self._extract_hooks()
        conflicts = self._extract_conflicts()
        insights = self._extract_insights()
        visual_moments = self._extract_visual_moments()
        climax = self._identify_climax()
        
        # Determine best structure
        structure_type = self._recommend_structure()
        
        # Organize into story beats
        setup_beats = self._organize_setup(hooks, conflicts)
        journey_beats = self._organize_journey(conflicts, visual_moments, insights)
        
        return StoryStructure(
            title=self._generate_title(),
            structure_type=structure_type,
            duration_target=self._estimate_duration(journey_beats),
            hooks=hooks[:3],  # Top 3 hooks
            setup_beats=setup_beats,
            journey_beats=journey_beats,
            climax=climax,
            insights=insights,
            visual_moments=visual_moments
        )
    
    def _extract_hooks(self) -> List[StoryElement]:
        """Extract potential video hooks from research"""
        hooks = []
        
        # Look for contradictions
        if "expectations" in self.data and "reality" in self.data:
            for exp, real in zip(self.data["expectations"], self.data["reality"]):
                if exp != real:
                    hooks.append(StoryElement(
                        element_type="hook_contradiction",
                        content=f"Expected: {exp} | Reality: {real}",
                        emotional_weight=8,
                        visual_potential=7,
                        timestamp_estimate="0:00-0:10",
                        tags=["contradiction", "surprising"]
                    ))
        
        # Look for bold claims
        if "unique_facts" in self.data:
            for fact in self.data["unique_facts"][:3]:
                hooks.append(StoryElement(
                    element_type="hook_bold_claim",
                    content=fact,
                    emotional_weight=7,
                    visual_potential=8,
                    timestamp_estimate="0:00-0:10",
                    tags=["unique", "interesting"]
                ))
        
        # Look for price surprises
        if "prices" in self.data:
            surprising_prices = [p for p in self.data["prices"] if "cheap" in p.lower() or "expensive" in p.lower()]
            for price in surprising_prices[:2]:
                hooks.append(StoryElement(
                    element_type="hook_price",
                    content=price,
                    emotional_weight=6,
                    visual_potential=5,
                    timestamp_estimate="0:00-0:10",
                    tags=["price", "practical"]
                ))
        
        # Sort by emotional weight
        return sorted(hooks, key=lambda x: x.emotional_weight, reverse=True)
    
    def _extract_conflicts(self) -> List[StoryElement]:
        """Extract challenges, obstacles, or tensions"""
        conflicts = []
        
        if "challenges" in self.data:
            for challenge in self.data["challenges"]:
                conflicts.append(StoryElement(
                    element_type="conflict",
                    content=challenge,
                    emotional_weight=7,
                    visual_potential=8,
                    timestamp_estimate="2:00-8:00",
                    tags=["challenge", "tension"]
                ))
        
        if "surprises" in self.data:
            for surprise in self.data["surprises"]:
                conflicts.append(StoryElement(
                    element_type="surprise",
                    content=surprise,
                    emotional_weight=6,
                    visual_potential=7,
                    timestamp_estimate="2:00-8:00",
                    tags=["unexpected", "interesting"]
                ))
        
        return conflicts
    
    def _extract_insights(self) -> List[StoryElement]:
        """Extract meaningful insights or lessons"""
        insights = []
        
        if "learnings" in self.data:
            for learning in self.data["learnings"]:
                insights.append(StoryElement(
                    element_type="insight",
                    content=learning,
                    emotional_weight=8,
                    visual_potential=5,
                    timestamp_estimate="8:00-10:00",
                    tags=["insight", "meaningful"]
                ))
        
        if "tips" in self.data:
            for tip in self.data["tips"]:
                insights.append(StoryElement(
                    element_type="practical_insight",
                    content=tip,
                    emotional_weight=6,
                    visual_potential=6,
                    timestamp_estimate="throughout",
                    tags=["practical", "helpful"]
                ))
        
        return insights
    
    def _extract_visual_moments(self) -> List[StoryElement]:
        """Extract visually compelling moments"""
        visual_moments = []
        
        if "locations" in self.data:
            for location in self.data["locations"]:
                visual_moments.append(StoryElement(
                    element_type="visual_location",
                    content=location,
                    emotional_weight=6,
                    visual_potential=9,
                    timestamp_estimate="throughout",
                    tags=["visual", "location"]
                ))
        
        if "experiences" in self.data:
            for exp in self.data["experiences"]:
                visual_moments.append(StoryElement(
                    element_type="visual_experience",
                    content=exp,
                    emotional_weight=7,
                    visual_potential=9,
                    timestamp_estimate="2:00-8:00",
                    tags=["experience", "action"]
                ))
        
        return sorted(visual_moments, key=lambda x: x.visual_potential, reverse=True)
    
    def _identify_climax(self) -> StoryElement:
        """Identify the most powerful moment for climax"""
        all_elements = (
            self._extract_conflicts() +
            self._extract_insights() +
            self._extract_visual_moments()
        )
        
        if not all_elements:
            return StoryElement(
                element_type="climax",
                content="[Climax to be determined based on filming]",
                emotional_weight=10,
                visual_potential=10,
                timestamp_estimate="8:00-9:00",
                tags=["climax", "peak"]
            )
        
        # Pick highest emotional weight + visual potential
        climax = max(all_elements, key=lambda x: x.emotional_weight + x.visual_potential)
        climax.element_type = "climax"
        climax.timestamp_estimate = "8:00-9:00"
        
        return climax
    
    def _recommend_structure(self) -> str:
        """Recommend the best narrative structure based on content"""
        has_journey = "journey" in str(self.data).lower()
        has_comparison = "vs" in str(self.data).lower() or "comparison" in str(self.data).lower()
        has_budget = "budget" in str(self.data).lower() or "cheap" in str(self.data).lower()
        has_time_limit = "hours" in str(self.data).lower() or "days" in str(self.data).lower()
        
        if has_comparison:
            return "Comparison Journey"
        elif has_budget:
            return "Budget Challenge"
        elif has_time_limit:
            return "Time-Lapse Journey (48 Hours In...)"
        elif has_journey:
            return "Hero's Journey"
        else:
            return "Discovery Arc"
    
    def _organize_setup(self, hooks: List[StoryElement], conflicts: List[StoryElement]) -> List[StoryElement]:
        """Organize setup beats (Act 1)"""
        setup = []
        
        # Context beat
        if "destination" in self.data:
            setup.append(StoryElement(
                element_type="context",
                content=f"Destination: {self.data['destination']}",
                emotional_weight=5,
                visual_potential=7,
                timestamp_estimate="0:10-0:45",
                tags=["setup", "context"]
            ))
        
        # Stakes beat (use first conflict if available)
        if conflicts:
            setup.append(conflicts[0])
        
        return setup
    
    def _organize_journey(self, conflicts: List[StoryElement], visual_moments: List[StoryElement], insights: List[StoryElement]) -> List[StoryElement]:
        """Organize journey beats (Act 2)"""
        # Interleave conflicts, visual moments, and insights
        journey = []
        
        # Add in varied order for interesting pacing
        for i in range(max(len(conflicts), len(visual_moments), len(insights))):
            if i < len(visual_moments):
                journey.append(visual_moments[i])
            if i < len(conflicts):
                journey.append(conflicts[i])
            if i < len(insights) and i % 2 == 0:  # Insights less frequently
                journey.append(insights[i])
        
        return journey[:8]  # Limit to 8 journey beats
    
    def _generate_title(self) -> str:
        """Generate a working title based on content"""
        if "destination" in self.data:
            dest = self.data["destination"]
            if "unique_facts" in self.data and self.data["unique_facts"]:
                return f"{dest}: {self.data['unique_facts'][0]}"
            return f"Exploring {dest}"
        return "Untitled Travel Video"
    
    def _estimate_duration(self, journey_beats: List[StoryElement]) -> str:
        """Estimate video duration based on content"""
        beat_count = len(journey_beats)
        
        if beat_count <= 3:
            return "6-8 minutes"
        elif beat_count <= 6:
            return "10-13 minutes"
        else:
            return "15-20 minutes"


def format_output(story: StoryStructure, format_type: str = "json") -> str:
    """Format story structure for output"""
    
    if format_type == "json":
        return json.dumps(asdict(story), indent=2)
    
    elif format_type == "markdown":
        md = f"# {story.title}\n\n"
        md += f"**Structure**: {story.structure_type}\n"
        md += f"**Target Duration**: {story.duration_target}\n\n"
        
        md += "## Hooks (Top 3)\n\n"
        for i, hook in enumerate(story.hooks, 1):
            md += f"{i}. **{hook.element_type}**: {hook.content}\n"
            md += f"   - Emotional Weight: {hook.emotional_weight}/10\n"
            md += f"   - Visual Potential: {hook.visual_potential}/10\n\n"
        
        md += "## Act 1: Setup Beats\n\n"
        for beat in story.setup_beats:
            md += f"- **{beat.element_type}** ({beat.timestamp_estimate}): {beat.content}\n"
        
        md += "\n## Act 2: Journey Beats\n\n"
        for i, beat in enumerate(story.journey_beats, 1):
            md += f"{i}. **{beat.element_type}** ({beat.timestamp_estimate})\n"
            md += f"   - {beat.content}\n"
            md += f"   - Tags: {', '.join(beat.tags)}\n\n"
        
        md += "## Act 3: Climax\n\n"
        md += f"**{story.climax.element_type}** ({story.climax.timestamp_estimate})\n\n"
        md += f"{story.climax.content}\n\n"
        
        md += "## Key Insights\n\n"
        for insight in story.insights[:5]:  # Top 5
            md += f"- {insight.content}\n"
        
        md += "\n## Visual Moments (Top 5)\n\n"
        for visual in story.visual_moments[:5]:
            md += f"- {visual.content} (Visual Potential: {visual.visual_potential}/10)\n"
        
        return md
    
    else:
        raise ValueError(f"Unknown format: {format_type}")


def main():
    parser = argparse.ArgumentParser(description="Analyze travel research for video storytelling")
    parser.add_argument("input", help="Input JSON file with research data")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", 
                       help="Output format")
    
    args = parser.parse_args()
    
    # Load research data
    try:
        with open(args.input, 'r') as f:
            research_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Analyze
    analyzer = TravelResearchAnalyzer(research_data)
    story = analyzer.analyze()
    
    # Format output
    output = format_output(story, args.format)
    
    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Story structure written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()

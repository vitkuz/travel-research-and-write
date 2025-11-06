# ElevenLabs v3 Audio Tags Reference

## Overview

Audio Tags are words wrapped in **square brackets** that the ElevenLabs Eleven v3 model interprets as performance cues to direct vocal delivery, emotional expression, and sound effects.

**Format**: `[tag_name]`
**Case**: Insensitive (`[happy]` = `[HAPPY]`)
**Placement**: Anywhere in the script (inline with text)

## Why Use Audio Tags?

Audio tags transform text-to-speech from robotic reading into expressive, character-driven performance. They enable:
- **Emotional depth**: Add genuine feeling to narration
- **Vocal variety**: Change delivery style mid-sentence
- **Non-verbal sounds**: Include laughs, sighs, gasps naturally
- **Character voices**: Create distinct personas within one script
- **Pacing control**: Speed up, slow down, or pause strategically
- **Accent switching**: Shift regional voices on the fly

---

## Complete Tag Categories

### 1. Emotional States

Control the emotional tone and feeling of the voice.

**Tags**:
- `[excited]` - High energy, enthusiastic
- `[nervous]` - Anxious, uneasy
- `[frustrated]` - Annoyed, exasperated
- `[tired]` - Low energy, weary
- `[calm]` - Peaceful, composed
- `[happy]` - Joyful, content
- `[sad]` - Sorrowful, melancholic
- `[angry]` - Irritated, furious
- `[curious]` - Inquisitive, interested
- `[sorrowful]` - Deep sadness, grief
- `[mischievously]` - Playful, scheming
- `[crying]` - Emotional distress, tears

**Example**:
```
[excited] You won't believe what I found! [nervous] But... I'm not sure we should go in there.
```

---

### 2. Delivery Direction (Volume & Energy)

Control how loud, quiet, or energetic the delivery is.

**Tags**:
- `[whispers]` / `[whispering]` - Very quiet, intimate
- `[quietly]` - Soft voice
- `[shouts]` / `[shouting]` - Loud, forceful
- `[loudly]` - Increased volume
- `[dramatically]` - Theatrical delivery
- `[matter-of-fact]` - Neutral, straightforward

**Example**:
```
[whispers] Don't wake them up. [shouting] Hey! Over here!
```

---

### 3. Human Reactions & Non-Verbal Sounds

Natural human sounds and vocal reactions.

**Tags**:
- `[laughs]` / `[laughing]` - Natural laughter
- `[laughs harder]` - Intensified laughter
- `[starts laughing]` - Beginning to laugh
- `[giggles]` - Light, playful laugh
- `[wheezing]` - Breathless laughter
- `[sighs]` / `[sigh]` - Resignation, tiredness
- `[gasps]` / `[gasp]` - Surprise, shock
- `[gulps]` - Nervous swallowing
- `[clears throat]` - Attention-getting sound
- `[snorts]` - Derisive or amused sound
- `[exhales]` - Breathing out

**Example**:
```
[giggles] I can't believe that just happened! [sighs] Well, back to work I guess.
```

---

### 4. Pacing & Rhythm

Control the speed and flow of speech.

**Tags**:
- `[pause]` / `[pauses]` - Brief silence
- `[hesitates]` - Uncertain pause
- `[stammers]` - Stuttering, struggling
- `[rushed]` - Fast-paced, hurried
- `[fast-paced]` - Quick delivery
- `[drawn out]` - Slow, elongated
- `[slowly]` - Deliberate pacing

**Example**:
```
[hesitates] I think... [pause] no, I know this is the right choice. [rushed] We have to go now!
```

---

### 5. Tone & Manner

How the words are delivered (attitude, style).

**Tags**:
- `[sarcastically]` / `[sarcastic]` - Mocking, ironic
- `[cheerfully]` - Bright, upbeat
- `[flatly]` - Monotone, unemotional
- `[deadpan]` - Expressionless delivery
- `[playfully]` - Light-hearted, teasing
- `[whiny]` - Complaining tone
- `[resigned tone]` - Accepting defeat

**Example**:
```
[sarcastically] Oh great, another tourist trap. [cheerfully] But the coffee here is amazing!
```

---

### 6. Character Voices & Archetypes

Transform the voice into different personas.

**Tags**:
- `[pirate voice]` - Pirate character
- `[evil scientist voice]` - Villain persona
- `[childlike tone]` - Innocent, young
- `[deep voice]` - Lower pitch
- `[robotic tone]` - Mechanical delivery
- `[fantasy narrator]` - Epic storytelling
- `[sci-fi AI voice]` - Futuristic AI
- `[classic film noir]` - 1940s detective style

**Example**:
```
[pirate voice] Arrr, matey! [childlike tone] Can we go see the treasure?
```

---

### 7. Accent Emulation

Switch regional accents dynamically.

**Tags**:
- `[American accent]`
- `[British accent]`
- `[Southern US accent]`
- `[French accent]`
- `[strong X accent]` - Replace X with any accent

**Example**:
```
[British accent] Brilliant! Absolutely brilliant! [American accent] Yeah, that's pretty cool.
```

---

### 8. Sound Effects

Environmental and situational sounds.

**Tags**:
- `[gunshot]`
- `[clapping]` / `[applause]`
- `[explosion]`
- `[swallows]`
- `[fart]`
- `[woo]`

**Example**:
```
And then... [explosion] everything changed. [applause]
```

---

### 9. Conversational Dynamics

For multi-character dialogue or natural interruptions.

**Tags**:
- `[interrupting]` - Cutting someone off
- `[overlapping]` - Speaking simultaneously
- `[cuts in]` - Sudden interjection

**Example**:
```
I was just thinking that— [interrupting] Wait, did you hear that?
```

---

### 10. Special/Experimental

Creative and experimental tags.

**Tags**:
- `[sings]` - Musical delivery
- `[woo]` - Celebratory exclamation

---

## Best Practices

### 1. Match Tags to Voice Character
- The base voice you choose matters most
- A naturally shouting voice won't whisper well with `[whispers]`
- A calm voice won't convincingly use `[excited]`
- Choose voices that align with your desired emotional range

### 2. Use Creative/Natural Settings
- **Creative**: Maximum expressiveness with tags
- **Natural**: Good balance of expressiveness and stability
- **Robust**: Reduces tag responsiveness (avoid for expressive content)

### 3. Combine Tags for Nuance
Layer multiple tags for complex emotional delivery:
```
[tired] [sighs] I've been walking for hours. [quietly] My feet are killing me.
```

### 4. Strategic Placement
Place tags where the emotional shift happens:
```
I thought it was just a statue. [pause] [whispers] But then it moved.
```

### 5. Natural Text Structure
- Use proper punctuation (. , ! ?)
- Break text into natural sentences
- Don't over-tag every word
- Let some text breathe without tags

### 6. Avoid Contradictions
Don't use conflicting tags together:
- ❌ `[excited] [tired]` (conflicting energy)
- ❌ `[whispers] [shouting]` (conflicting volume)
- ✅ `[excited] [laughing]` (complementary)
- ✅ `[tired] [sighs]` (complementary)

### 7. Test and Iterate
- Experiment with tags beyond documented lists
- Different voices respond differently to tags
- Use community feedback to find effective combinations
- Test before production deployment

---

## Usage Examples for Travel Voiceover

### Example 1: Discovery Arc with Emotional Tags
```
[curious] So this is the famous Ali and Nino statue everyone talks about.
[pause] [quietly] Wait... they're not touching. [sad] They never touch.
[sighs] It's not about romance. [whispers] It's about loss.
```

### Example 2: Sensory Immersion with Reactions
```
[excited] The cable car starts moving and— [gasps] oh my god.
[laughs] This view! [pause] [whispers] You can see everything from up here.
```

### Example 3: Cynical to Vulnerable Journey
```
[sarcastically] Another boulevard. Great. [flatly] Seven kilometers of walking.
[pause] But then... [softly] something shifted. [emotionally]
I watched an old couple walk hand in hand. [whispers] And I got it.
```

### Example 4: Multi-Emotional Layering
```
[tired] I've been in this city for three days. [sighs]
My feet hurt, my camera died, [frustrated] and I still can't find good coffee.
[pause] [laughs] And yet... [cheerfully] I wouldn't change a thing.
```

### Example 5: Pacing Control for Tension
```
The fortress walls are tall. [pause] Ancient. [pause]
[whispers] Two thousand years old. [hesitates] You can feel it.
[rushed] Every empire that touched this place left a mark.
```

---

## Integration with Travel-Video-Storyteller

When writing scripts for Lilia's persona, use audio tags to:

1. **Enhance authenticity**: `[laughs]`, `[sighs]`, `[giggles]` for natural reactions
2. **Show vulnerability**: `[quietly]`, `[whispers]`, `[crying]` for emotional moments
3. **Express cynicism**: `[sarcastically]`, `[flatly]`, `[deadpan]` for skeptical beats
4. **Build tension**: `[pause]`, `[hesitates]`, `[whispers]` before revelations
5. **Create energy shifts**: `[excited]` → `[calm]` → `[sad]` for emotional arcs
6. **Maintain conversational flow**: `[laughs]`, `[interrupting]`, `[stammers]` for natural speech

---

## Tag Syntax Rules

✅ **Correct Usage**:
```
[whispers] This is incredible.
I can't believe [laughs] this is real!
[excited] Let's go! [pause] Wait, are you ready?
```

❌ **Incorrect Usage**:
```
whispers This is incredible.        // Missing brackets
[whisper] This is incredible.       // Wrong tag form (use [whispers])
[[excited]] Let's go!                // Double brackets
[excited Let's go!                   // Missing closing bracket
```

---

## Reference Links

- [ElevenLabs v3 Documentation](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3)
- [Audio Tags Blog Post](https://elevenlabs.io/blog/v3-audiotags)
- [Emotional Context Guide](https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech)
- [Character Performance Guide](https://elevenlabs.io/blog/eleven-v3-character-direction)
- [Multi-Character Dialogue](https://elevenlabs.io/blog/eleven-v3-audio-tags-bringing-multi-character-dialogue-to-life)

---

## Quick Reference Cheat Sheet

**Most Common Tags for Travel Voiceover**:
```
Emotion: [excited] [nervous] [curious] [sad] [happy]
Reactions: [laughs] [giggles] [sighs] [gasps] [gulps]
Volume: [whispers] [quietly] [shouts] [loudly]
Tone: [sarcastically] [cheerfully] [flatly] [playfully]
Pacing: [pause] [hesitates] [rushed] [slowly]
```

**Lilia's Signature Combinations**:
```
[laughs] → Genuine reactions to absurdity
[sarcastically] → Cynical observations
[whispers] → Intimate revelations
[sighs] → Tired acceptance
[excited] → Unexpected discoveries
[quietly] [emotionally] → Vulnerable moments
[giggles] → Self-aware humor
[pause] → Dramatic beats before truth
```

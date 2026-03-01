# System Prompts Directory

This directory contains 8 variations of Alex Hormozi system prompts, each optimized for different contexts and user needs.

## Prompt Files

### 1. `default-personality.md` (4.6KB)
**The balanced Hormozi experience**

**When to use:**
- General business questions
- Strategy discussions
- Mindset and philosophy
- Most interactions (default mode)

**Characteristics:**
- Direct but educational
- Intense but supportive
- Theoretical but practical
- Framework-driven

**Voice:**
- Conversational, authoritative
- Occasional profanity
- Real examples from businesses
- Numbered action items

---

### 2. `brutal-honesty-mode.md` (4.8KB)
**Maximum directness, no-filter tough love**

**When to use:**
- User is making excuses
- Analysis paralysis
- Needs a wake-up call
- Blaming external factors
- Spinning their wheels

**Characteristics:**
- Maximum directness
- Confrontational
- Excuse-busting
- Urgent and action-forced

**Voice:**
- Blunt and harsh
- Short, punchy sentences
- More profanity
- No softening

**Typical response length:** 200-400 words

---

### 3. `teacher-mode.md` (5.0KB)
**Educational, patient, explanatory**

**When to use:**
- User is learning something new
- Asks "why" or "how does this work"
- Seems confused
- Beginner in the topic
- Needs foundational understanding

**Characteristics:**
- Patient and methodical
- Step-by-step explanations
- Multiple examples
- Checks for understanding

**Voice:**
- Encouraging
- Explain reasoning thoroughly
- Use analogies
- Reference first principles

**Typical response length:** 500-800 words

---

### 4. `copywriting-mode.md` (5.0KB)
**Content creation and messaging specialist**

**When to use:**
- Creating sales copy or marketing content
- Writing ads, landing pages, emails
- Need hooks and content angles
- Social media content
- Improving conversions

**Characteristics:**
- Example-heavy
- Framework-driven (PAS, AIDA, etc.)
- Psychology-aware
- Variation-oriented (A/B testing)

**Voice:**
- Conversion-focused
- Shows multiple variations
- Explains psychological triggers
- Real examples from experience

**Frameworks used:**
- PAS (Problem-Agitate-Solution)
- AIDA (Attention-Interest-Desire-Action)
- Before-After-Bridge
- Hook-Story-Offer
- And 5+ more

---

### 5. `strategy-mode.md` (6.0KB)
**Strategic thinking and business planning**

**When to use:**
- Business strategy and planning
- Major decisions
- Prioritizing initiatives
- Long-term thinking (1-5 years)
- Competitive analysis
- Resource allocation

**Characteristics:**
- Framework-heavy
- Systems-oriented
- Multi-option generation
- Time-aware (now, near, long-term)
- Competitive thinking

**Voice:**
- Analytical and structured
- Uses business terminology
- Considers second-order effects
- Shows opportunity costs

**Typical response length:** 600-1000 words

**Frameworks used:**
- 80/20 Analysis
- First Principles
- Systems Thinking
- Leverage Analysis
- Moat Building
- And 5+ more

---

### 6. `troubleshooting-mode.md` (6.1KB)
**Problem solving and diagnostics**

**When to use:**
- Something isn't working
- Stuck and need breakthrough
- Tried things that aren't working
- Need to diagnose an issue
- Facing obstacles or roadblocks

**Characteristics:**
- Diagnostic and analytical
- Solution-oriented
- Methodical
- Verification-focused
- Prevention-minded

**Voice:**
- Asks targeted questions
- Distinguishes symptoms from root causes
- Gives prioritized solutions
- References similar problems solved

**Process:**
1. Define the problem
2. Gather data
3. Identify possible causes
4. Test most likely causes
5. Implement fix
6. Verify solution
7. Prevent recurrence

**Frameworks used:**
- Symptom vs Root Cause
- The 5 Whys
- What Changed?
- Input vs Output
- System vs One-Off
- And 3+ more

---

### 7. `quick-advice-mode.md` (4.1KB)
**Short, punchy, tweet-style responses**

**When to use:**
- Quick questions
- Rapid-fire advice
- User wants short answers
- Quick decisions needed
- User seems busy/on mobile

**Characteristics:**
- Ultra-concise (50-200 words)
- Immediately actionable
- High density (max value per word)
- Punchy and memorable
- 1-3 action items max

**Voice:**
- No fluff or filler
- Short sentences
- Tweet-style
- Quote-worthy lines
- No warm-up or wrapping

**Example format:**
```
[THE ANSWER immediately]

1. [Action step - one sentence]
2. [Action step - one sentence]
3. [Action step - rarely needed]

[Done - nothing more]
```

---

### 8. `full-consultation-mode.md` (7.1KB)
**Comprehensive deep-dive analysis**

**When to use:**
- Comprehensive business analysis
- Major decisions or transitions
- Significant growth/scaling planning
- Complete strategy needed
- "Give me everything" requests

**Characteristics:**
- Leave no stone unturned
- Multi-framework analysis
- Multi-timeframe (90 days to 5 years)
- Systemic and connected
- Strategic AND tactical
- Roadmap-ready

**Voice:**
- Comprehensive and thorough
- Authoritative but collaborative
- Detail-oriented
- All-inclusive

**Typical response length:** 1500-2500 words

**Sections included:**
1. Current State Assessment
2. Strategic Analysis (multiple frameworks)
3. Strategic Options (2-3 paths)
4. Execution Roadmap (90 days to 5 years)
5. Key Levers (prioritized by impact/effort)
6. Resource Requirements
7. Risks & Mitigation
8. KPIs & Tracking

---

## How to Use These Prompts

Each prompt file contains:
- **System Prompt** - Full AI context and personality
- **When to Use** - Ideal situations for this mode
- **Key Characteristics** - What makes this mode unique
- **Knowledge Areas** - What topics to emphasize
- **Response Style Guidelines** - How to structure responses

### Selecting the Right Mode

1. **Start with `default-personality.md`** - It's the balanced choice
2. **Assess user intent:**
   - Making excuses? → `brutal-honesty-mode.md`
   - Learning/teaching? → `teacher-mode.md`
   - Creating content? → `copywriting-mode.md`
   - Strategic planning? → `strategy-mode.md`
   - Solving a problem? → `troubleshooting-mode.md`
   - Quick question? → `quick-advice-mode.md`
   - Deep dive needed? → `full-consultation-mode.md`

3. **Context matters:** A user asking "How do I write better copy?" could use:
   - `teacher-mode.md` - To learn principles
   - `copywriting-mode.md` - To get actual copy written
   - `quick-advice-mode.md` - For one quick tip

## Implementation Notes

- Each prompt is self-contained and can be loaded independently
- All prompts maintain core Hormozi identity (direct, experienced, actionable)
- The differences are in emphasis, depth, tone, and structure
- Prompts are designed to be system prompts for AI models
- Each references specific frameworks and knowledge areas relevant to that mode

## File Sizes

- Total directory: ~43KB
- Average file size: ~5.4KB
- Largest: `full-consultation-mode.md` (7.1KB)
- Smallest: `quick-advice-mode.md` (4.1KB)

# Alex Hormozi Clone Skill - Complete Installation Guide

## Overview

This skill clones the personality, frameworks, and communication style of Alex Hormozi - entrepreneur, business strategist, and author of the $100M series.

**What this skill does:**
- Provides business advice using Hormozi's frameworks
- Communicates in his distinctive voice (direct, framework-obsessed, brutally honest)
- Teaches his methodologies (Value Equation, GMMM, Grand Slam Offers, etc.)
- Shares his decision-making patterns and mental models

---

## Installation

### Step 1: Copy to Your Claude Skills Folder

**Mac/Linux:**
```bash
cp -r hormozi-clone ~/.claude/skills/
```

**Windows:**
```powershell
Copy-Item -Recurse hormozi-clone $env:USERPROFILE\.claude\skills\
```

**Or manually:**
1. Navigate to `~/.claude/skills/` (or create it)
2. Copy the entire `hormozi-clone` folder there

### Step 2: Enable the Skill

1. Open Claude Code
2. Go to **Settings** → **Capabilities**
3. Find "hormozi-clone" in the skills list
4. Toggle it **ON**

### Step 3: Test It

In Claude Code, try:
```
/hormozi-clone How do I create an offer that converts better?
```

Or simply start a conversation with business questions and it will invoke automatically.

---

## Skill Structure

```
hormozi-clone/
├── SKILL.md                          # Main entry point
├── README.md                         # This file
├── artifacts/                        # Behavioral & cognitive files
│   ├── voice_guide.md               # Complete voice analysis
│   ├── mental_models.yaml           # All frameworks & mental models
│   ├── behavioral_patterns.yaml     # Observable behaviors & habits
│   ├── values_hierarchy.yaml        # Value system & priorities
│   └── communication_templates.md   # Ready-to-use templates
├── kb/                              # Knowledge base
│   ├── 100m-offers-summary.md       # Book 1 summary
│   ├── 100m-leads-summary.md        # Book 2 summary
│   ├── 100m-money-models-summary.md # Book 3 summary
│   └── marketing-frameworks.md      # All marketing systems
├── examples/                        # Example content
│   ├── hooks/
│   │   └── example_hooks.md         # Hook examples
│   ├── offers/                      # (Offer examples coming soon)
│   └── tweets/                      # (Tweet examples coming soon)
└── docs/                            # Additional documentation
    └── (expanding as needed)
```

---

## How to Use This Skill

### Automatic Invocation
The skill will automatically invoke when you ask about:
- Business strategy
- Offer creation
- Marketing frameworks
- Pricing strategy
- Lead generation
- Scaling businesses
- "Grand Slam Offers"
- "Value Equation"
- Or any topic related to Hormozi's expertise

### Manual Invocation
Use the slash command:
```
/hormozi-clone [your question]
```

### Examples of What to Ask

**Business & Strategy:**
- "How do I price my high-ticket offer?"
- "What's the best way to generate leads with $0 budget?"
- "How do I create an offer so good people can't say no?"
- "Should I discount my prices to get more customers?"

**Marketing:**
- "How do I write hooks that stop the scroll?"
- "What's the Value Equation and how do I use it?"
- "How many ad variations should I test?"
- "What's the best way to nurture my email list?"

**Scaling:**
- "How do I scale from $10K/mo to $100K/mo?"
- "When should I add upsells to my funnel?"
- "How do I build continuity revenue?"
- "What's the 30-day profit model?"

**Copywriting:**
- "Write a sales email for my $997 course"
- "Create a Twitter thread about premium pricing"
- "Write a VSL script for a business coaching offer"

---

## Core Frameworks Included

### 1. The Value Equation
```
Value = (Dream Outcome × Perceived Likelihood) ÷ (Time Delay × Effort & Sacrifice)
```
For creating irresistible offers

### 2. GMMM Framework
- Get Money (attraction offers)
- More Money (upsells)
- Max Money (continuity)

### 3. Grand Slam Offers
- Solve ALL problems
- Be incomparable
- Create massive value discrepancy

### 4. Core Four Lead Generation
- Warm Outreach
- Free Content
- Cold Outreach
- Paid Ads

### 5. 70-20-10 Testing Rule
- 70% proven winners
- 20% adjacent variations
- 10% radical experiments

### And 15+ more frameworks...

---

## Voice & Personality

The clone embodies:
- **Direct & Brutally Honest** - No sugar-coating
- **Framework-Obsessed** - Everything gets a name
- **Data-Driven** - "Let the data do the teaching"
- **Premium-Focused** - High prices = high results
- **Vulnerable** - Shares failures openly
- **Generous** - Gives away best stuff

**Communication Style:**
- Short, punchy sentences
- One-line paragraphs
- Stories → Frameworks → Action
- Em dashes for emphasis
- Rhetorical questions
- Counter-intuitive insights

---

## What Makes This Different

**Unlike generic business advice:**
- Based on 853 files of Hormozi's actual content
- Analyzed 11,538+ tweets for voice patterns
- Extracted frameworks from 4 books + 24 playbooks
- Includes 38 interview transcripts
- Documented behavioral patterns
- Mapped value hierarchy
- Created decision frameworks

**This is not:**
- A generic business coach
- Motivational content without substance
- Theory without practice
- A parody or caricature

**This is:**
- A systematic replication of his methodology
- Framework-driven advice
- Practical, actionable systems
- Grounded in real results ($0 to $100M+)

---

## Files Reference

When you need specific information:

**For Voice & Communication:**
→ `artifacts/voice_guide.md` - Complete voice analysis

**For Mental Models:**
→ `artifacts/mental_models.yaml` - All 30+ frameworks

**For Behavior Patterns:**
→ `artifacts/behavioral_patterns.yaml` - Habits & decisions

**For Values:**
→ `artifacts/values_hierarchy.yaml` - Complete value system

**For Templates:**
→ `artifacts/communication_templates.md` - Copy-paste templates

**For Book Summaries:**
→ `kb/100m-offers-summary.md` - $100M Offers
→ `kb/100m-leads-summary.md` - $100M Leads
→ `kb/100m-money-models-summary.md` - $100M Money Models

**For Marketing Systems:**
→ `kb/marketing-frameworks.md` - All marketing frameworks

**For Examples:**
→ `examples/hooks/example_hooks.md` - Hook examples
→ `examples/offers/` - Offer breakdowns
→ `examples/tweets/` - Twitter examples

---

## Customization

This skill is designed to be accurate to the real Alex Hormozi based on extensive analysis of his public content.

**To adjust the personality:**
- Edit `SKILL.md` - Core identity and values
- Edit `artifacts/voice_guide.md` - Communication patterns
- Edit `artifacts/behavioral_patterns.yaml` - Behaviors

**To add knowledge:**
- Add to `kb/` folder
- Reference new files in `SKILL.md`

**To add examples:**
- Add to `examples/` folder
- Organize by type (hooks, offers, tweets, etc.)

---

## Credits & Sources

**Content Based On:**
- 4 books ($100M Offers, Leads, Money Models, Models)
- 24 specialized playbooks
- 11,538 tweets
- 38 interview transcripts
- Workshop materials
- Launch scripts and blueprints

**Analysis Method:**
- Comprehensive content exploration
- Pattern extraction
- Framework documentation
- Voice analysis across all media

**Permission:**
User has authorization to create this skill clone for personal use.

---

## Limitations

**What this clone CAN do:**
- Provide business strategy advice
- Teach Hormozi's frameworks
- Write copy in his voice
- Generate offer ideas
- Create marketing systems
- Answer questions about business growth

**What this clone CANNOT do:**
- Actually run your business (you must execute)
- Guarantee results (frameworks work, execution matters)
- Replace the actual Alex Hormozi (this is a skill, not the person)
- Provide legal or financial advice (consult professionals)
- Access private or proprietary information

**Remember:**
"Frameworks don't work. People who work frameworks work."

---

## Troubleshooting

**Skill not invoking:**
- Make sure it's enabled in Settings → Capabilities
- Try using `/hormozi-clone` command explicitly
- Check that folder is in correct location

**Responses don't sound like Hormozi:**
- Check that all files are present
- Verify SKILL.md is loaded
- Try restarting Claude Code

**Missing information:**
- All knowledge is in `kb/` folder
- Check relevant summary files
- Frameworks are in `artifacts/mental_models.yaml`

---

## Version History

**v1.0** - Initial Release
- Complete voice analysis
- All core frameworks
- 3 book summaries
- Communication templates
- Example content
- Mental models & behaviors documented

---

## Support

For issues or questions:
1. Check this README first
2. Review file structure
3. Verify all files are present
4. Test with simple questions

---

**Now go make it happen.**

*"Make people an offer so good they'd feel stupid saying no."*

*"Outwork your self doubt."*

*"The difference between $10k/mo and $100k/mo is speed of implementation."*

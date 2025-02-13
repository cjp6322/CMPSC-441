# Prompt Engineering Process

## Step 1: Initial Implementation
### Goal
Set up the base chat flow for the Dungeon Master (DM) agent

### What I Changed
Used the `ollama.chat` function to enable message exchange between the user and the DM. Ensured responses were appended to maintain context.

### Result
Basic interaction was functional, allowing the user to engage in a DnD session.

### Reflection
The initial setup worked as expected, but responses lacked depth and consistency in storytelling.

---

## Step 2: Refining the System Prompt
### Intention
Improve the DM’s ability to maintain game rules, track combat, and ensure logical consistency.

### Action/Change
Remade the prompt to extensively go over:
- NPC and environmental control
- Skill checks and difficulty classes
- Combat mechanics
- Logical world consistency

### Result
The DM became more structured, but still isn't perfect. I'm not sure if it's my prompt or my small-sized LLM holding it back

### Reflection
Adding explicit rules improved gameplay but made some interactions feel rigid. Future iterations could balance structure and flexibility.

---

## Step 3: Combat Flow Adjustments
### Intention
Make combat mechanics smoother and more engaging.

### Action/Change
- Defined initiative order and turn-based structure.
- Ensured HP tracking for characters and NPCs.
- Enforced attack roll and AC comparisons.

### Result
Combat interactions became more rule-compliant but slowed down dialogue.

### Reflection
Combat worked well but felt a bit mechanical. Future refinements could streamline responses for better pacing.

---

## Step 4: Enhancing User Experience
### Intention
Improve the overall flow and immersion.

### Action/Change
- Added adventure selection at the start.
- Allowed users to define their character stats.
- Tweaked response style for better engagement.

### Result
A more immersive and interactive experience.

### Reflection
These changes made the game more engaging, but balancing response length and conciseness remains a challenge.

---

## Conclusion
The iterative improvements significantly enhanced the DM agent's effectiveness. Further refinements could focus on balancing structure, pacing, and adaptability.
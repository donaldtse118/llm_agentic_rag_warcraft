# llm_agentic_rag_warcraft
 A simple LLM agentic RAG projects with warcraft theme.
Demostrated LLM thining propose and leverage private information and tool to conduct a task of actual damage calculation.


# Components
This tool is a damage calculator designed for World of Warcraft (WoW) classes by using LLM agentic-RAG

Key components:
1. Private informaiton **wow_doc**: 
    - Provides information about WoW classes, such as "paladin".
    - Specifies the skills available to the class and their respective `damage formula`.

2. **Functions Tools**:
    They are in nested relationship
    - `warcraft_tool.charactor` to get class's stats `strength`
    - `warcraft_tool.calculator` convert `strength` to `attack power`
    - `warcraft_tool.calculator` calculate `actual damage` by `attack power` and `damage formula`


## Expected results
LLM would think and find out 2 skills from `wow_doc` and character'stats and calculate `actual damage` as follow:

1. Skill: Crusader Strike
   - Actual Damage = 107% x Attack power 
   - Actual Damage = 107% x (Strength * 2 - 20) <-- LLM found strength to attack power formula from tool
   - Actual Damage = 107% x (80 * 2 - 20)  <-- LLM found character's strength to 80 from tool
   - Actual Damage = 107% x 140
   - Actual Damage = 149.8

2. Skill: Templar's Verdict
   - Actual Damage = 146% x Attack power 
   - Actual Damage = 146% x (Strength * 2 - 20) <-- LLM found strength to attack power formula from tool
   - Actual Damage = 146% x (80 * 2 - 20)  <-- LLM found character's strength to 80 from tool
   - Actual Damage = 146% x 140
   - Actual Damage = 204.4


## Sample ouptut
(formatted a bit for markdown display, raw output at the button of main.py)

Q: According to my character paladin stats, calculate the each skill per row, with columns `actual damage` in number , `damage formula`
---------------------------------------
A: (from **Agentic** engine)...thinking
- Running step 90bdf98d-ad3b-4caf-8070-9a6626da9839. 
  - Step input: According to my character paladin stats, calculate the each skill per row, with columns `actual damage` in number , `damage formula`
  - Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
  - Action: query_tool
  - Action Input: {'input': 'paladin skills damage formula'}
  - Observation: The damage formula for the Paladin skill Crusader Strike is (107% of Attack Power) x 1. The damage formula for the Paladin skill Templar's Verdict is 146% of Attack Power.

- Running step e2cdef9a-72f6-44d5-8742-5de49b84e706. 
  - Step input: None
  - Thought: I need to use a tool to help me answer the question.
  - Action: lookup_stats_for_character
  - Action Input: {'character': 'paladin'}
  - Observation: {'strength': 80, 'agility': 10}

- Running step 49678ce5-3ae3-486a-9147-ac0753c73f65. 
  - Step input: None
  - Thought: I need to use a tool to help me answer the question.
  - Action: convert_strength_to_attack_power
  - Action Input: {'strength': 80}
  - Observation: 140


- Running step 0b6fe76e-362f-442a-8d90-2e9a488db0dd. 
  - Step input: None
  - Thought: I need to use a tool to help me answer the question.
  - Action: calculate_actual_damage
  - Action Input: {'multiplier': '107%', 'attack_power': 140}
  - Observation: 149

- Running step 1f84de96-1c3c-4cd6-93e4-f3ad6e249652. 
  - Step input: None
  - Thought: I can answer without using any more tools. I'll use the user's language to answer
  - Answer: | Skill | Actual Damage | Damage Formula |
|---|---|---|
| Crusader Strike | 149 | (107% of Attack Power) x 1 |
| Templar's Verdict | 204.4 | 146% of Attack Power |

- A: (from **Agentic** engine): 

| Skill | Actual Damage | Damage Formula |
|---|---|---|
| Crusader Strike | 149 | (107% of Attack Power) x 1 |
| Templar's Verdict | 204.4 | 146% of Attack Power |

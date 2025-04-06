# builtin

# 3rd parties
from llama_index.core import VectorStoreIndex
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.agent import ReActAgent

# local
from setup import init
from documents import wow_doc
from warcraft_tool import character as char
from warcraft_tool import calculator as cal


# Setup the LLM and embedding model
init.setup_llm_and_embedding()



# Build the index using the in-memory documents
documents = wow_doc.get_paladin_skills()
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()


# Agentic : Setup agent with function tools
wow_skill_tool = FunctionTool.from_defaults(
    fn=cal.convert_strength_to_attack_power,
    name="convert_strength_to_attack_power",
    description="Performs conversion from strength to attack power"
)

wow_dmg_tool = FunctionTool.from_defaults(
    fn=cal.calculate_actual_damage,
    name="calculate_actual_damage",    
    description="Calculate actual damage by multiplier and attack power, e.g. `150% of attack power`"
)

wow_char_tool = FunctionTool.from_defaults(
    fn=char.lookup_stats_for_character,
    name="lookup_stats_for_character",
    description="Lookup character's stats, e.g. strength, aglity"
)

query_engine_tool = QueryEngineTool.from_defaults(
    query_engine=query_engine,
    name="query_tool",
    description="Query what skills available and its description about damage formula"    
)


agent = ReActAgent.from_tools([wow_skill_tool,
                               wow_dmg_tool,
                               wow_char_tool,
                               query_engine_tool],
                               verbose=True,                               
                               max_interations=20,
                               )

# You could try reduce information provided from questions to see if the agent can leverage the suitable tools to answer
questions = [
            # "Give my retribution paladin got 100 attack power, show the each skills in table format, with columns `calculated actual damages made` , `formula`" ,
            # "Given my paladin got 80 strength, show the each skills in table format, with columns `calculated actual damages made` , `formula`" ,
            # "For my character paladin, show the each skills in table format, with columns `calculated actual damages made` , `formula`" ,
            "According to my character paladin stats, calculate the each skill per row, with columns `actual damage` in number , `damage formula`" ,
]



for question in questions:
    print(f"######################################")
    print(f"Q: {question}")
    print(f"---------------------------------------")

    ## For agentic
    print(f"A: (from **Agentic** engine)...thinking")    
    response = agent.chat(question)
    print(f"A: (from **Agentic** engine): {response}")    
    

    print(f"######################################")
    print(f"")


######################################
# A: (from **Agentic** engine)...thinking
# > Running step 90bdf98d-ad3b-4caf-8070-9a6626da9839. Step input: According to my character paladin stats, calculate the each skill per row, with columns `actual damage` in number , `damage formula`
# Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
# Action: query_tool
# Action Input: {'input': 'paladin skills damage formula'}
# Observation: The damage formula for the Paladin skill Crusader Strike is (107% of Attack Power) x 1. The damage formula for the Paladin skill Templar's Verdict is 146% of Attack Power.
# > Running step e2cdef9a-72f6-44d5-8742-5de49b84e706. Step input: None
# Thought: I need to use a tool to help me answer the question.
# Action: lookup_stats_for_character
# Action Input: {'character': 'paladin'}
# Observation: {'strength': 80, 'agility': 10}
# > Running step 49678ce5-3ae3-486a-9147-ac0753c73f65. Step input: None
# Thought: I need to use a tool to help me answer the question.
# Action: convert_strength_to_attack_power
# Action Input: {'strength': 80}
# Observation: 140
# > Running step 0b6fe76e-362f-442a-8d90-2e9a488db0dd. Step input: None
# Thought: I need to use a tool to help me answer the question.
# Action: calculate_actual_damage
# Action Input: {'multiplier': '107%', 'attack_power': 140}
# Observation: 149
# > Running step 1f84de96-1c3c-4cd6-93e4-f3ad6e249652. Step input: None
# Thought: I can answer without using any more tools. I'll use the user's language to answer
# Answer: | Skill | Actual Damage | Damage Formula |
# |---|---|---|
# | Crusader Strike | 149 | (107% of Attack Power) x 1 |
# | Templar's Verdict | 204.4 | 146% of Attack Power |
# A: (from **Agentic** engine): | Skill | Actual Damage | Damage Formula |
# |---|---|---|
# | Crusader Strike | 149 | (107% of Attack Power) x 1 |
# | Templar's Verdict | 204.4 | 146% of Attack Power |
######################################
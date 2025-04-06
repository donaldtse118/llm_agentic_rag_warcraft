# builtin
import os

# 3rd parties
from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.core import Settings

COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

EMBEDDING_MODEL = "embed-english-v3.0"
LLM_MODEL = "command-r-plus"

_LLM = None
_EMBEL_MODEL = None

def setup_llm_and_embedding():

    global _LLM, _EMBEL_MODEL
    # Create LLM instance
    if not _LLM:
        _LLM = Cohere(
            api_key=COHERE_API_KEY,
            model=LLM_MODEL,    
            temperature=0.2,
            # add since agentic
            system_prompt="""Use ONLY the provided context and generate a complete, coherent answer to the user's query. 
            Your response must be grounded in the provided context and relevant to the essence of the user's query.
            """
        )
        Settings.llm = _LLM

    # Create embedding model instance
    if not _EMBEL_MODEL:    
        _EMBEL_MODEL = CohereEmbedding(
            api_key=COHERE_API_KEY,
            model_name=EMBEDDING_MODEL,
            input_type="search_document"
        )
        Settings.embed_model = _EMBEL_MODEL
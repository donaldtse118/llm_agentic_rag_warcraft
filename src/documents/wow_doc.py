# inbuilt
from typing import List

# 3rd parties
from llama_index.core import Document


def get_paladin_skills() -> List[Document]:
    """
    For simply skip web crawl but copy paladin skills description and create document instances, included
    - skill name
    - damage formula e.g. 107% of Attack power * 1 (while how to calculate Attack power is another problem)

    Returns:
        List[Document]: list of llama index documents
    """

    documents = [
        Document(doc_id="crusader_strike",
                 text="skill: crusader strike, cost: 1.6% of base mana, Melee Range, Strike the target for [(107% of Attack power) * 1], Blades of Light: Holystrike / Physica damage."),
        Document(doc_id="templars_verdict",
                 text="skill: templar's verdict, cost 3 Holy Power, Unleashes a powerful weapon strike that deals (146% of Attack power) [Blades of Light: Holystrike / Holy] damage to an enemy target.")
    ]

    return documents

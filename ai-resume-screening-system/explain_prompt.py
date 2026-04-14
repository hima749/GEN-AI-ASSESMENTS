from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["match_data", "score"],
    template="""
Explain why this candidate received this score.

Score: {score}
Match Data: {match_data}

Give a short explanation.
"""
)
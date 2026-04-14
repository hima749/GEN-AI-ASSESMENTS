from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
You are an AI assistant evaluating a candidate.

Based on the matching results, assign a score from 0 to 100.

Criteria:
- More matching skills → higher score
- Missing important skills → lower score

Return ONLY a number.

Match Data:
{match_data}
"""
)
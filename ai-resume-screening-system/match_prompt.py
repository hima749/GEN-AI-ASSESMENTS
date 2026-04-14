from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["extracted_data", "job_description"],
    template="""
You are an AI assistant that compares a candidate's profile with a job description.

Identify:
1. Matching skills
2. Missing skills

Return in JSON format:
{{
  "matching_skills": [],
  "missing_skills": []
}}

Candidate Data:
{extracted_data}

Job Description:
{job_description}
"""
)
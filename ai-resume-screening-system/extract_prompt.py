from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI assistant that extracts structured information from resumes.

Extract the following:
1. Skills
2. Experience (in years, if mentioned)
3. Tools/Technologies

Return output in STRICT JSON format:
{{
  "skills": [],
  "experience": "",
  "tools": []
}}

Rules:
- Do NOT assume anything not mentioned in the resume
- Do NOT add extra fields
- If something is missing, return empty list or empty string

Resume:
{resume}
"""
)
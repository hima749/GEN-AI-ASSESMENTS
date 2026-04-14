from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.score_prompt import score_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100,
    temperature=0.1,
    repetition_penalty=1.2,   # ✅ stops repetition
    do_sample=False           # ✅ more controlled output
)

llm = HuggingFacePipeline(pipeline=pipe)

score_chain = score_prompt | llm
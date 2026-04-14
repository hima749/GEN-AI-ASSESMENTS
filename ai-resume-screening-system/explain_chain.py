from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.explain_prompt import explain_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100,
    repetition_penalty=1.2,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

explain_chain = explain_prompt | llm
from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------------------------
# INPUT DATA
# -------------------------

resume = """
John Doe
Skills: Python, Machine Learning, SQL
Experience: 2 years in data analysis
Tools: Pandas, Scikit-learn, Excel
"""

job_description = """
Looking for a Data Scientist with skills in Python, Machine Learning, Deep Learning, SQL.
Experience with tools like Pandas, TensorFlow, and Scikit-learn required.
"""

# -------------------------
# STEP 1: EXTRACT
# -------------------------

result = extract_chain.invoke({"resume": resume})

print("\n========== EXTRACTED ==========")
print(result)

# -------------------------
# STEP 2: MATCH
# -------------------------

matched = match_chain.invoke({
    "extracted_data": str(result)[:500],   # ✅ trimmed to avoid token overflow
    "job_description": job_description
})

print("\n========== MATCH RESULT ==========")
print(matched)

# -------------------------
# STEP 3: SCORE
# -------------------------

score = score_chain.invoke({
    "match_data": str(matched)[:500]   # ✅ trimmed
})

print("\n========== SCORE ==========")
print(score)

# -------------------------
# STEP 4: EXPLANATION
# -------------------------

explanation = explain_chain.invoke({
    "match_data": str(matched)[:500],   # ✅ trimmed
    "score": str(score)
})

print("\n========== EXPLANATION ==========")
print(explanation)
"""Streamlit demo for LLM Evaluation Lab. Run: streamlit run app.py"""
import streamlit as st
from src.evaluation.evaluator import score_response
from src.evaluation.metrics import weighted_score

st.title("LLM Evaluation Lab")
st.write("Paste a response, enter expected keywords, and get a rubric score.")
response = st.text_area("Response", "Photosynthesis lets plants use sunlight and water to make glucose and oxygen.")
keywords = st.text_input("Expected keywords (comma-separated)", "photosynthesis, sunlight, glucose")
if st.button("Evaluate"):
    kw = [k.strip() for k in keywords.split(",") if k.strip()]
    scores, error = score_response(response, kw)
    st.write(f"Weighted score: **{weighted_score(scores)} / 100**")
    st.write(f"Error type: **{error}**")
    st.json(scores)

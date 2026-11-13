"""Scoring rubric for LLM responses.

Weights are experimental defaults. Calibrate them on a held-out
set with human annotators before using them for decisions.
"""
WEIGHTS = {
    "factual_accuracy": 0.30,
    "instruction_following": 0.25,
    "relevance": 0.20,
    "completeness": 0.15,
    "clarity": 0.10,
}

ERROR_TYPES = ["hallucination", "relevance", "omission", "instruction_failure", "none"]

def describe(score_1_to_5):
    return {5: "Excellent", 4: "Good", 3: "Fair", 2: "Poor", 1: "Bad"}.get(score_1_to_5, "Unknown")

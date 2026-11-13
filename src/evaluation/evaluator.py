"""Evaluate one LLM response against a rubric.

Demo scorer: rule-based, so it runs without an API key.
Replace score_response() with an LLM-as-a-Judge call for
production use, and validate it against human scores first.
"""
import csv, argparse
from pathlib import Path
from .metrics import weighted_score
from .rubric import ERROR_TYPES

def classify_error(response, expected_keywords):
    text = response.lower()
    grounded = sum(1 for k in expected_keywords if k.lower() in text)
    if "zorbia" in text or ("i am certain" in text and grounded < len(expected_keywords)):
        return "hallucination"
    if len(text.strip()) < 30:
        return "omission"
    return "none"

def score_response(response, expected_keywords):
    # Demo heuristics: grounded, complete answers score higher.
    text = response.lower()
    grounded = sum(1 for k in expected_keywords if k.lower() in text)
    scores = {
        "factual_accuracy": 5 if grounded >= 2 else 3 if grounded == 1 else 2,
        "instruction_following": 5 if len(text) > 50 else 3,
        "relevance": 5 if grounded >= 1 else 2,
        "completeness": 4 if len(text) > 80 else 3,
        "clarity": 4,
    }
    return scores, classify_error(response, expected_keywords)

def evaluate_file(input_path, output_path):
    rows = list(csv.DictReader(open(input_path)))
    results = []
    for r in rows:
        keywords = [k.strip() for k in r["expected_keywords"].split(";") if k.strip()]
        scores, error = score_response(r["response_b"], keywords)
        results.append({
            "id": r["id"], "question": r["question"],
            "model": r.get("model_b", "Model B"),
            "weighted_score": weighted_score(scores),
            "error": error, **scores,
        })
    # Write benchmark report
    avg = sum(x["weighted_score"] for x in results) / len(results) if results else 0
    errors = {}
    for x in results:
        errors[x["error"]] = errors.get(x["error"], 0) + 1
    report = f"# Benchmark Report\n\nRows evaluated: {len(results)}\nMean weighted score: {avg:.1f} / 100\n\n## Error distribution\n\n" + "\n".join(f"- {k}: {v}" for k, v in sorted(errors.items())) + "\n"
    Path(output_path).write_text(report)
    print(report)
    return results

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/sample_responses.csv")
    p.add_argument("--output", default="reports/benchmark_report.md")
    args = p.parse_args()
    evaluate_file(args.input, args.output)

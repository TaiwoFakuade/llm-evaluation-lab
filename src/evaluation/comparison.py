"""Pairwise comparison: A vs B."""
from .metrics import weighted_score

def compare(scores_a, scores_b):
    wa, wb = weighted_score(scores_a), weighted_score(scores_b)
    if wa > wb:
        return "A", wa, wb
    if wb > wa:
        return "B", wa, wb
    return "tie", wa, wb

def win_rate(results):
    """results: list of 'A'/'B'/'tie' winners. Returns dict."""
    n = len(results) or 1
    return {k: round(results.count(k) / n, 2) for k in ["A", "B", "tie"]}

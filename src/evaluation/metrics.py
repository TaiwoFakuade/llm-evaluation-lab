"""Weighted scoring and inter-rater agreement."""
from .rubric import WEIGHTS

def weighted_score(scores):
    """scores: dict dimension -> 1-5. Returns 0-100 weighted score."""
    total = sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)
    return round(total / 5 * 100, 1)

def cohens_kappa(a_labels, b_labels):
    """Simple Cohen's kappa for two annotators on categorical labels."""
    assert len(a_labels) == len(b_labels) and len(a_labels) > 0
    n = len(a_labels)
    observed = sum(1 for a, b in zip(a_labels, b_labels) if a == b) / n
    labels = sorted(set(a_labels) | set(b_labels))
    expected = sum(
        (sum(1 for x in a_labels if x == lab) / n) * (sum(1 for x in b_labels if x == lab) / n)
        for lab in labels
    )
    if expected == 1:
        return 1.0
    return round((observed - expected) / (1 - expected), 3)

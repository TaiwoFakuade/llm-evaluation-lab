from src.evaluation.metrics import weighted_score, cohens_kappa
from src.evaluation.comparison import compare, win_rate

def test_weighted_score_perfect():
    scores = {"factual_accuracy": 5, "instruction_following": 5, "relevance": 5, "completeness": 5, "clarity": 5}
    assert weighted_score(scores) == 100.0

def test_weighted_score_weights():
    scores = {"factual_accuracy": 5, "instruction_following": 1, "relevance": 1, "completeness": 1, "clarity": 1}
    # 0.30*5 + 0.70*1 = 2.2 / 5 * 100 = 44.0
    assert weighted_score(scores) == 44.0

def test_cohens_kappa_perfect():
    assert cohens_kappa(["a", "b", "a"], ["a", "b", "a"]) == 1.0

def test_compare_a_wins():
    a = {"factual_accuracy": 5, "instruction_following": 5, "relevance": 5, "completeness": 5, "clarity": 5}
    b = {"factual_accuracy": 1, "instruction_following": 1, "relevance": 1, "completeness": 1, "clarity": 1}
    winner, wa, wb = compare(a, b)
    assert winner == "A" and wa > wb

def test_win_rate():
    assert win_rate(["A", "A", "B", "tie"]) == {"A": 0.5, "B": 0.25, "tie": 0.25}

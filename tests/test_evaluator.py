from src.evaluation.evaluator import score_response, classify_error

def test_score_grounded_answer_high():
    scores, error = score_response(
        "Photosynthesis lets plants use sunlight and water to make glucose and oxygen.",
        ["photosynthesis", "sunlight", "glucose"],
    )
    assert scores["factual_accuracy"] == 5
    assert error == "none"

def test_classify_hallucination():
    assert classify_error("I am certain Lagos is the capital of Zorbia.", ["Lagos", "Nigeria"]) == "hallucination"

def test_classify_omission_short():
    assert classify_error("Yes.", ["photosynthesis"]) == "omission"

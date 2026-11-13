# LLM Evaluation Lab

An end-to-end framework for evaluating LLM responses against structured quality criteria — factual accuracy, instruction following, relevance, completeness, and clarity.

Built for AI Evaluation, LLM Quality Analyst, and RLHF roles. All data is synthetic.

## Why this exists

AI models can sound convincing while being wrong, ignoring instructions, or answering a question that was never asked. This lab measures those failures systematically, with a rubric, pairwise comparison, error classification, and a benchmark report — not just a single score.

## Scoring framework

| Dimension | Weight |
|---|---|
| Factual accuracy | 30% |
| Instruction following | 25% |
| Relevance | 20% |
| Completeness | 15% |
| Clarity | 10% |

Weights are documented experimental defaults, not universal standards. See `src/evaluation/rubric.py` for how to calibrate them.

Error types: `hallucination`, `relevance`, `omission`, `instruction_failure`, `none`.

## Run it

```bash
pip install -r requirements.txt
python -m src.evaluation.evaluator --input data/sample_responses.csv --output reports/benchmark_report.md
python -m pytest -q
```

Or try the demo dashboard:
```bash
pip install streamlit
streamlit run app.py
```

## Structure

```
llm-evaluation-lab/
├── src/evaluation/
│   ├── rubric.py        # scoring dimensions and weights
│   ├── metrics.py       # weighted scoring, agreement
│   ├── evaluator.py     # evaluate one response, classify errors
│   └── comparison.py    # pairwise A vs B, win-rate
├── data/sample_responses.csv
├── tests/test_evaluator.py
├── tests/test_metrics.py
├── reports/sample_evaluation_report.md
├── .github/workflows/ci.yml
├── app.py
├── requirements.txt
└── LICENSE
```

## Sample result

See `reports/sample_evaluation_report.md` — on the 3-row synthetic sample, mean weighted score is 80.7 / 100, with 1 hallucination and 2 clean responses. Your results will differ on real data; the point is the method is reproducible.

## Limitations

- The default scorer in this repo is rule-based for demonstration, so it can run without an API key. Swap in an LLM-as-a-Judge in `evaluator.py` for production use, and measure human-vs-automated agreement (Cohen's kappa) before trusting it.
- Synthetic data only. Do not upload employer, client, or proprietary evaluation data.

## Skills

LLM evaluation, rubric design, pairwise ranking, error analysis, Python, pytest, GitHub Actions, Streamlit.

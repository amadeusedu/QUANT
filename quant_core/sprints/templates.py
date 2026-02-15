TEMPLATES = {
    "momentum_replication": "Replicate simple momentum strategy.",
    "mean_reversion": "Test mean reversion baseline.",
    "factor_model": "Replicate one-factor model.",
    "options_toy": "Binomial vs Black-Scholes toy pricing.",
    "microstructure": "Spread-impact stylized study.",
}

MEMO_TEMPLATE = """# Sprint Memo: {sprint_id}
## 1) Objective & Hypothesis
{hypothesis}
## 2) Data & Assumptions
{data}
## 3) Method
{method}
## 4) Results
{results}
## 5) Robustness Checks
{robustness}
## 6) Failure Modes
{failures}
## 7) Next Steps
{next_steps}
"""

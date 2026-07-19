# Project Title

One-sentence description of the problem and outcome.

## Problem

What question are you answering? Who would care about the result?

## Dataset

- Source:
- Size / features:
- How to obtain: (link or download steps — do not commit large raw files)

## Approach

- Models / methods used
- Feature engineering or preprocessing highlights
- Evaluation metrics

## Results

Summarize the main findings (table or bullet points). Link to key figures in `reports/figures/` if useful.

## How to run

```bash
# from the repository root
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r projects/<project-folder>/requirements.txt
jupyter lab
```

Open the notebooks under `notebooks/` in order (if numbered). Charts should use the shared style in `common/portfolio_style.py`.

## Project layout

```
.
├── README.md
├── requirements.txt
├── notebooks/          # analysis & modeling notebooks
├── src/                # reusable Python modules
├── data/
│   ├── raw/            # original data (gitignored)
│   └── processed/      # cleaned features (gitignored)
├── models/             # saved model artifacts (gitignored)
└── reports/
    └── figures/        # charts worth showing in the README
```

## Checklist

- [ ] Problem and results clearly documented
- [ ] Notebook cleaned and runnable end-to-end
- [ ] Plots use `common/portfolio_style.py`
- [ ] Requirements pinned enough to reproduce

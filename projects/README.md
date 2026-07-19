# Projects

Each folder under `projects/` is a standalone machine learning project.

## Current projects

| Folder | Summary |
|--------|---------|
| [`fashion-coat-dress-classification/`](fashion-coat-dress-classification/) | Coat vs dress binary classification with SVM / Naive Bayes / LDA and PCA / LLE |

## Adding a project

1. Copy `projects/_template/` to a new folder, e.g. `projects/customer-churn-prediction/`.
2. Fill in that project's `README.md` (problem, approach, results, how to run).
3. Put notebooks in `notebooks/` and reusable code in `src/`.
4. Use the shared plot style from [`common/portfolio_style.py`](../common/portfolio_style.py).
5. Document data sources; keep large datasets out of git unless they ship with the project.
6. List the project in the root [README](../README.md).

## Naming

Prefer short, descriptive kebab-case names:

- `house-price-regression`
- `image-classifier-cnn`
- `nlp-sentiment-analysis`

# Projects

Each folder under `projects/` is a standalone machine learning project.

## Current projects

| Folder | Summary |
|--------|---------|
| [`fashion-coat-dress-classification/`](fashion-coat-dress-classification/) | Coat vs dress binary classification with SVM / Naive Bayes / LDA and PCA / LLE |

## How to add a project

1. Copy `projects/_template/` to a new folder, e.g. `projects/customer-churn-prediction/`.
2. Rename and fill in that project's `README.md` (problem, approach, results, how to run).
3. Put notebooks in `notebooks/` and reusable code in `src/`.
4. Keep large datasets out of git unless they are small enough to ship with the project — document how to obtain them otherwise.
5. Add a short entry for the project in the root [README](../README.md).

## Suggested naming

Use short, descriptive kebab-case names that sound like product/problem titles:

- `house-price-regression`
- `image-classifier-cnn`
- `nlp-sentiment-analysis`

Avoid course codes or assignment numbers in folder names.

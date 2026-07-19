# Machine Learning Portfolio

Machine learning projects by **Chaya Trachová**.

Each project lives under [`projects/`](projects/) as a self-contained Python / Jupyter notebook study — problem framing, methods, results, and how to reproduce them.

## Projects

| Project | Topic | Status |
|---------|-------|--------|
| [Fashion Coat vs Dress Classification](projects/fashion-coat-dress-classification/) | Binary image classification + PCA/LLE | Complete |

## Stack

- Python 3.10+
- Jupyter Lab / Notebook
- NumPy, pandas, scikit-learn, matplotlib, seaborn

Shared plotting style: [`common/portfolio_style.py`](common/portfolio_style.py).  
Per-project dependencies live in that project's `requirements.txt`. A shared baseline is in the root [`requirements.txt`](requirements.txt).

## Setup

```bash
git clone https://github.com/trachcha/machine-learning-portfolio.git
cd machine-learning-portfolio

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r projects/fashion-coat-dress-classification/requirements.txt

# optional: register the kernel for Jupyter
python -m ipykernel install --user --name=ml-portfolio --display-name="Python 3 (.venv)"

jupyter lab
```

Open any notebook under `projects/<project-name>/notebooks/` and choose the **Python 3 (.venv)** kernel.

The `.venv` folder is gitignored — recreate it on each machine with the commands above.

## Continuous integration

A GitHub Actions workflow re-executes project notebooks on pushes to `main` when notebooks, data, shared style, or requirements change (and can also be run manually). Successful runs commit updated notebook outputs and figures back to the repository.

The fashion classification notebook includes full hyperparameter sweeps, so the first CI run can take a long time.

## Repository layout

```
machine-learning-portfolio/
├── README.md
├── requirements.txt
├── common/                     # shared style & utilities
├── projects/
│   ├── README.md
│   ├── _template/              # starter layout for new projects
│   └── fashion-coat-dress-classification/
└── ...
```

## Author

**Chaya Trachová**  
chaya.trachova@gmail.com

# Machine Learning Portfolio

Portfolio of machine learning projects by **Chaya Trachová**.

Each project lives in its own folder under [`projects/`](projects/), written in Python with Jupyter notebooks, and framed as an independent piece of work — problem, approach, results, and how to reproduce it.

## Projects

| Project | Topic | Status |
|---------|-------|--------|
| [Fashion Coat vs Dress Classification](projects/fashion-coat-dress-classification/) | Binary image classification + PCA/LLE | Complete |

Copy [`projects/_template/`](projects/_template/) when you add a new project, then list it in the table above.

## Stack

- Python 3.10+
- Jupyter Lab / Notebook
- NumPy, pandas, scikit-learn, matplotlib, seaborn

Per-project dependencies live in that project's `requirements.txt`. A shared baseline is in the root [`requirements.txt`](requirements.txt).

## Setup (virtual environment)

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

Then open any notebook under `projects/<project-name>/notebooks/` and choose the **Python 3 (.venv)** kernel.

The `.venv` folder is gitignored — recreate it on each machine with the commands above.

## Project structure

```
machine-learning-portfolio/
├── README.md
├── requirements.txt
├── .venv/                      # local only (not committed)
├── projects/
│   ├── README.md
│   ├── _template/              # starter layout for new work
│   └── fashion-coat-dress-classification/
└── ...
```

## Author

**Chaya Trachová**  
chaya.trachova@gmail.com

# Machine Learning Portfolio

Portfolio of machine learning projects by **Chaya Trachová**.

Each project lives in its own folder under [`projects/`](projects/), written in Python with Jupyter notebooks, and framed as an independent piece of work — problem, approach, results, and how to reproduce it.

## Projects

| Project | Topic | Status |
|---------|-------|--------|
| _(coming soon)_ | — | — |

Copy [`projects/_template/`](projects/_template/) when you add a new project, then list it in the table above.

## Stack

- Python 3.10+
- Jupyter Lab / Notebook
- NumPy, pandas, scikit-learn, matplotlib, seaborn

Per-project dependencies live in that project's `requirements.txt`. A shared baseline is in the root [`requirements.txt`](requirements.txt).

## Setup

```bash
git clone https://github.com/trachcha/machine-learning-portfolio.git
cd machine-learning-portfolio
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open any notebook under `projects/<project-name>/notebooks/`.

## Project structure

```
machine-learning-portfolio/
├── README.md
├── requirements.txt
├── projects/
│   ├── README.md
│   ├── _template/          # starter layout for new work
│   └── <project-name>/     # one folder per project
└── ...
```

## Author

**Chaya Trachová**  
chaya.trachova@gmail.com

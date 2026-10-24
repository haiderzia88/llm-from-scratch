# LLM From Scratch (Python Files Only)

Learn the foundations of a GPT-style large language model through **10 chapters**.
All lesson programs and exercises use plain **`.py` files**, not Jupyter notebooks.

> **Current status:** Chapter 01 is ready to run. Chapters 02–10 are intentionally starter files for future lessons. We will gradually build a tiny GPT-style model after understanding the foundations.

## Our 10-concept checklist

- [ ] 01. Python and NumPy — **in progress**
- [ ] 02. Mathematics for LLMs
- [ ] 03. Neural Networks
- [ ] 04. PyTorch
- [ ] 05. Tokenization
- [ ] 06. Embeddings
- [ ] 07. Attention Mechanism
- [ ] 08. Transformer Architecture
- [ ] 09. Model Training
- [ ] 10. Text Generation

## Start here (VS Code / terminal)

Requires **Python 3.10+**.

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python chapters/01_python_numpy/01_python_basics.py
python chapters/01_python_numpy/02_numpy_arrays.py
python chapters/01_python_numpy/03_matrix_multiplication.py
```

macOS/Linux (replace activation line):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python chapters/01_python_numpy/01_python_basics.py
```

Complete `chapters/01_python_numpy/exercises.py` by replacing the TODOs, then run it.

Test numerical examples:

```bash
python -m unittest discover -s tests -v
```

## Project folders

- `chapters/` — one folder for each learning concept. The first chapter includes working demonstrations and exercises. Other chapters contain `.py` lesson placeholders, not completed implementations.
- `src/mini_gpt/` — reserved for reusable GPT architecture, training, and generation modules we will develop later.
- `data/` — reserved for small, properly licensed training data; large files should not be committed.
- `tests/` — automated tests.

## GitHub

Recommended repository name: `llm-from-scratch`

Recommended description: `Build and understand a GPT-style LLM from scratch using Python, NumPy and PyTorch.`

Create an empty repository on GitHub (without an auto-generated README), then run these commands **inside the extracted `llm-from-scratch-py` folder**:

```bash
git init -b main
git add .
git commit -m "Start LLM from scratch with Python lessons"
git remote add origin https://github.com/YOUR_USERNAME/llm-from-scratch.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. If your repository already exists, use the appropriate existing remote and branch instead.

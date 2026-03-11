# numerical-methods

A modular Python implementation of core numerical methods including root-finding, interpolation, integration, ODE and linear systems solvers.
Work in progress — structured for future expansion.

- For an overview of the repository layout, see [Project Structure](docs/project_structure.md).

- For the required libraries and packages, see [Requirements](requirements.txt)

## Phase I : Root Finder

This phase implements numerical algorithms for solving nonlinear equations of the form:

```Code
f(x) = 0
```

Each method iteratively approximates a root within a specified tolerance. The implementations are modular, configurable, and return structured results including convergence history for further analysis or visualization.

### Implemented Methods

Click on the links below to view the source code implementations of each method.

- [Bisection](src/num_methods/roots/bisection.py)
- [False Position](src/num_methods/roots/false_position.py)
- [Newton–Raphson](src/num_methods/roots/newton_raphson.py)
- [Secant](src/num_methods/roots/secant.py)
- [Hybrid (Bisection + Newton)](src/num_methods/roots/hybrid_bisec_NR.py)

## ⚙️ Installation & Setup

### Create a virtual environment

```Bash
python -m venv venv
```

### Activate (PowerShell)

```Bash
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```Bash
pip install -r requirements.txt
```

### Run

From project root:

```Bash
$env:PYTHONPATH="src"  
python -m num_methods.main
```

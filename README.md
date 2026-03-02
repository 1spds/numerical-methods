# numerical-methods

A modular Python implementation of core numerical methods including root-finding, interpolation, integration, ODE and linear systems solvers.
Work in progress — structured for future expansion.

## Phase I : Root Finder

This phase implements numerical algorithms for solving nonlinear equations of the form:

```Code
f(x) = 0
```

Each method iteratively approximates a root within a specified tolerance. The implementations are modular, configurable, and return structured results including convergence history for further analysis or visualization.

## Implemented Methods

- Bisection
- False Position
- Newton–Raphson
- Secant
- Hybrid (Bisection + Newton)

## Project Structure

```Code
numerical-methods/
│
├── README.md
├── requirements.txt
├── src/
│   └── num_methods/
│       ├── roots/
│       │   │── __init__.py
│       │   ├── bisection.py
│       │   ├── false_position.py
│       │   ├── newton.py
│       │   ├── secant.py
│       │   └── hybrid.py
│       │
│       ├── config.py
│       ├── main.py
│       └── __init__.py
```

### ⚙️ Installation & Setup

#### Create a virtual environment

```Bash
python -m venv venv
```

#### Activate (PowerShell)

```Bash
.\venv\Scripts\Activate.ps1
```

#### Install dependencies

```Bash
pip install -r requirements.txt
```

### Run

From project root:

```Bash
$env:PYTHONPATH="src"  
python -m num_methods.main
```

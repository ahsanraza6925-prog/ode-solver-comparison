# Numerical Comparison of Explicit and Implicit ODE Solvers

## Project Overview

This project compares four established numerical methods for solving ordinary differential equations (ODEs): RK45, DOP853, Radau, and BDF.

The Van der Pol oscillator is used to investigate how changing the parameter μ affects computational effort and numerical accuracy.

## Research Question

How does increasing the parameter μ affect the computational effort and numerical error of explicit and implicit ODE solvers?

## Mathematical Model

The Van der Pol oscillator is described by:

\[
\frac{dx}{dt}=z
\]

\[
\frac{dz}{dt}=\mu(1-x^2)z-x
\]

Initial conditions:
- x(0) = 2
- z(0) = 0

Parameter values:
- μ = 1
- μ = 50

## Numerical Methods

The following solvers were compared:

- **RK45:** Explicit Runge–Kutta method
- **DOP853:** High-order explicit Runge–Kutta method
- **Radau:** Implicit Runge–Kutta method
- **BDF:** Implicit multistep method

## Evaluation Metrics

- Function evaluations (nfev)
- Jacobian evaluations (njev)
- LU decompositions (nlu)
- Wall-clock runtime
- Maximum absolute difference from a high-accuracy numerical reference

## Tools Used

- Python
- NumPy
- SciPy
- pandas
- Matplotlib

## Repository Files

- `ode_solver_benchmark.py` — Python implementation
- `ode_solver_benchmark_results.csv` — Numerical results
- `ode_solver_effort.png` — Comparison of solver function evaluations

## Key Findings

In the recorded experiment, DOP853 used the fewest function evaluations for μ = 1, while BDF used the fewest for μ = 50.

These findings apply only to the tested model, parameter settings, tolerances, and computing environment. The results do not establish that one solver is universally superior.

## How to Run

Install the required packages:

```bash
pip install numpy scipy pandas matplotlib
```

Run the script:

```bash
python ode_solver_benchmark.py
```

The script generates a CSV results file and visualizations.

## Limitations

This project is a small, reproducible comparison of established numerical methods. It does not introduce a new numerical algorithm. Further work could include additional differential-equation models, tolerance sensitivity analysis, and repeated runtime measurements.

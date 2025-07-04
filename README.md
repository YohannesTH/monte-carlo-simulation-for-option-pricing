# Monte Carlo Simulation for European Option Pricing

This project implements a Monte Carlo simulation to estimate the price of **European call and put options**, and compares the results to the analytical solution provided by the **Black-Scholes model**. It also visualizes the convergence behavior as the number of simulations increases.

---

## Overview

Monte Carlo methods are widely used in quantitative finance to estimate the value of options and other derivatives, especially when analytical solutions are not available. In this project:

- We simulate the underlying asset price paths using **Geometric Brownian Motion (GBM)**
- Use the **risk-neutral pricing formula** to compute option prices
- Compare the Monte Carlo estimates with the **Black-Scholes closed-form solution**
- Visualize how the Monte Carlo estimate converges as the number of simulations increases

---

## Tools and Technologies

- Python 3
- NumPy
- Matplotlib
- Black-Scholes Model (Analytical Formula)

---

## Features

- Simulates European call and put option prices
- Implements vectorized Monte Carlo simulations for performance
- Compares Monte Carlo results to Black-Scholes formula
- Visualizes convergence of simulated prices as `n → ∞`
- Modular and easy to understand

---

## Project Structure

```text
monte-carlo-option-pricing/
│
├── monte_carlo_pricing.py        # Monte Carlo simulation implementation
├── black_scholes.py              # Analytical Black-Scholes functions
├── convergence_plot.png          # Output: convergence visualization
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

# plot_convergence.py

import numpy as np
import matplotlib.pyplot as plt
from monte_carlo_pricing import monte_carlo_option_price
from black_scholes import black_scholes_call_price

S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
option = 'call'

bs_price = black_scholes_call_price(S0, K, T, r, sigma)

sim_counts = np.logspace(2, 5, 20, dtype=int)
estimates = [monte_carlo_option_price(S0, K, T, r, sigma, n, option) for n in sim_counts]

plt.figure(figsize=(10, 6))
plt.plot(sim_counts, estimates, label='Monte Carlo Estimate', marker='o')
plt.axhline(bs_price, color='r', linestyle='--', label='Black-Scholes Price')
plt.xscale('log')
plt.xlabel('Number of Simulations (log scale)')
plt.ylabel('Option Price')
plt.title('Convergence of Monte Carlo Simulation to Black-Scholes Price')
plt.legend()
plt.grid(True)
plt.savefig('convergence_plot.png')
plt.show()

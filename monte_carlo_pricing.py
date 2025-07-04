# monte_carlo_pricing.py

import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, n_sim=10000, option='call'):
    np.random.seed(0)
    Z = np.random.standard_normal(n_sim)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)

    discounted_payoff = np.exp(-r * T) * payoff
    return np.mean(discounted_payoff)

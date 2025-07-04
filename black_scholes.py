# black_scholes.py

from math import log, sqrt, exp
from scipy.stats import norm

def black_scholes_call_price(S, K, T, r, sigma):
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    return call

def black_scholes_put_price(S, K, T, r, sigma):
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    put = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put

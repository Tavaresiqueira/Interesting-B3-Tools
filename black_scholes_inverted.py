from scipy.optimize import newton
import numpy as np
from scipy.stats import norm

#  a funcao normal para calcular o preco de uma call atraves das variaveis tradicionais todo mundo ja tem em maos
# mas eh interessante ter uma funcao para calcular a volatilidade atraves do preco atual do derivativo, ou seja, fazer a inversa, afim de encontrar a volatilidade implicita atual

#black and scholes simples para calcular o valor de uma call
def black_scholes(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    call = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    return call

#encontrando a volatilidade implicita do ativo que esta sendo precificada pelo mercado por meio do preco da call 
def implied_volatility(S, K, T, r, option_price):
    def difference(sigma):
        return black_scholes(S, K, T, r, sigma) - option_price

    initial_volatility = 0.2
    return newton(difference, initial_volatility)

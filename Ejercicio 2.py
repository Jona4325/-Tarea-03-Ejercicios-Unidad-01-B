import math

def calcular_n_arctan(error_max):
    n = 1
    P_n = 0
    while abs(4 * P_n - math.pi) >= error_max:
        term = (-1)**(n+1) / (2*n - 1)
        P_n += term
        n += 1
    return n

# Prueba para |4Pn(1) - pi| < 10^-3
n_10e_3 = calcular_n_arctan(1e-3)
print("Número de términos para error < 10^-3:", n_10e_3)

# Prueba para |4Pn(1) - pi| < 10^-10
n_10e_10 = calcular_n_arctan(1e-10)
print("Número de términos para error < 10^-10:", n_10e_10)

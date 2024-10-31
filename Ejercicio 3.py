def calcular_n_pi_identidad(error_max):
    P1 = 0
    P2 = 0
    n = 1
    while abs(4 * (4 * P1 - P2) - math.pi) >= error_max:
        term1 = (-1)**(n+1) / (2*n - 1) / 5**(2*n - 1)
        term2 = (-1)**(n+1) / (2*n - 1) / 239**(2*n - 1)
        P1 += term1
        P2 += term2
        n += 1
    return n

# Prueba para |4 * (4P1 - P2) - pi| < 10^-3
n_pi = calcular_n_pi_identidad(1e-3)
print("Número de términos para aproximación de pi con error < 10^-3:", n_pi)

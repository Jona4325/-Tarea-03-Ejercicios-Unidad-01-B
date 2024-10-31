def calcular_suma_anidada(a, b):
    suma_total = 0
    mult_count = 0
    sum_count = 0
    n = len(a)
    
    for i in range(n):
        for j in range(i + 1):
            suma_total += a[i] * b[j]
            mult_count += 1
            sum_count += 1
    
    return suma_total, mult_count, sum_count

a = [1, 2, 3] 
b = [4, 5, 6]
suma_total, mult_count, sum_count = calcular_suma_anidada(a, b)

print("Suma total:", suma_total)
print("Número de multiplicaciones:", mult_count)
print("Número de sumas:", sum_count)

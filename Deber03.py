import math

def SerieMaclaurin(): 
    tolerancia = 10**-10
    serie = 0
    i = 0
    iteracionmax=1000000
    while (abs((4 * serie) - math.pi) > tolerancia) and (i<iteracionmax):
        serie += ((-1) ** i) / (2 * i + 1)
        i += 1
        print(i)
    return i 

def SerieMaclaurinArtan(): 
    pi_calculado = 0
    n = 0
    tolerancia = 10**-3

    while True:
        termino_1 = ((-1) ** n) / (5 ** (2 * n + 1)) / (2 * n + 1)
        termino_2 = ((-1) ** n) / (239 ** (2 * n + 1)) / (2 * n + 1)

        pi_calculado += ( (16*termino_1 - 4*termino_2))
        
        print(f"Iteración {n}: |π calculado - π real| = {abs(pi_calculado - math.pi)}")
        if abs(pi_calculado - math.pi) < tolerancia:
            break
        
        n += 1
    
    print(f"Iteraciones totales: {n}, Aproximación de π: {pi_calculado}")
    return pi_calculado

def calcular_suma(a, b):
    total_sum = 0
    n = len(a)  
    
    for i in range(1, n + 1): 
        for j in range(1, i + 1): 
            producto = a[0] * b[j - 1]  
            total_sum += producto  
    
    return total_sum

def calcular_suma_optimizacion(a, b):
    n = len(a)  
    s = [0] * (n + 1)  
    for i in range(n, 0, -1):  
        s[i] = a[i - 1] + s[i + 1]  
    total_sum = 0
    for j in range(1, n + 1): 
        total_sum += b[j - 1] * s[j]  

    return total_sum

def lado_derecho(x):
    return (1 + 2 * x) / (1 + x + x**2)

def termino(i, x):
    numerator = 2**i * x**(i + 1)  
    denominator = 1 - x**(2**i) + x**(2**(i + 1)) 
    return numerator / denominator

def calcular_terminos(x):
    suma_izquierda = 0
    diferencia = float('inf')  
    n_terminos = 0
    lado_derecho_valor = lado_derecho(x)  

    while diferencia > 10**-6:  
        n_terminos += 1  
        suma_izquierda += termino(n_terminos - 1, x)  
        diferencia = abs(suma_izquierda - lado_derecho_valor)  

    return n_terminos

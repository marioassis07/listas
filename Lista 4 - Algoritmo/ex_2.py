def potencia(a, n):
    if n == 0:          
        return 1
    return a * potencia(a, n - 1)


print(potencia(2,3))
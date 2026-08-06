def somar_ate_zero():
    soma = 0
    while True:
        numero = float(input("Digite um número (0 para parar): "))
        if numero == 0:
            break
        soma += numero
    return soma

resultado = somar_ate_zero()
print(f"A soma dos valores digitados é: {resultado}")
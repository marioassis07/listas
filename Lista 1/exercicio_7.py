#Exercício 7
def ler_numeros(quantidade):
    numeros = []
    for i in range(quantidade):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)
    return numeros

nums = ler_numeros(10)
soma = sum(nums)
media = soma / len(nums)

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
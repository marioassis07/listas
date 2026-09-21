def anagramas(s):
    if len(s) <= 1:              
        return [s]
    resultado = []
    for i in range(len(s)):
        letra = s[i]                     
        resto = s[:i] + s[i+1:]          
        for sub in anagramas(resto):     
            resultado.append(letra + sub)   
    return resultado

print(anagramas("abc"))

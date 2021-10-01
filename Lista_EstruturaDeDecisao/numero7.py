numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
numero3 = float(input("Digite o terceiro numero:"))

numeros = [numero1, numero2, numero3]
menorNumero = min(numeros)
maiorNumero = max(numeros)

# for x in numeros:
#     if maiorNumero < x:
#         maiorNumero = x

print("menor numero:", menorNumero)
print("maior numero:", maiorNumero)
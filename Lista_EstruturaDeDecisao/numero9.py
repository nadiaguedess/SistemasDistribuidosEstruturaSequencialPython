numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
numero3 = float(input("Digite o terceiro numero:"))

lista = [numero1, numero2, numero3]
lista.sort(reverse=True)

print("Numeros organizados:")
for x in lista:
    print(x)




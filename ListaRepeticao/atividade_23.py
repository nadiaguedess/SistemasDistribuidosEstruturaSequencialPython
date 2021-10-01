usuario = int(input("Digite um numero inteiro: "))


for x in range(1,usuario):
    contador = 0
    for y in  range(1,x+1):
        if (x % y == 0):
            contador += 1
    if (contador == 2):
        print("esse numero é primo:", x)
    else:
        print("esse numero não e primo", x)

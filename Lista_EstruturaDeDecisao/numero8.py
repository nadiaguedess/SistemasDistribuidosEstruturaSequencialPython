produto1 = float(input("Digite o preço do primeiro produto:"))
produto2 = float(input("Digite o preço do segundo produto:"))
produto3 = float(input("Digite o preço do terceiro produto:"))

precos = [produto1, produto2, produto3]
menorNumero = min(precos)

if menorNumero == produto1:
    print("Produto 1 é o mais barato", produto1)

elif menorNumero == produto2:
    print("Produto 2 é o mais barato:", produto2)
else:
    print("Produto 3 é o mais barato:", produto3)

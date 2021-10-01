pesoDoPeixe = float(input("Digite o peso do peixe:"))

if pesoDoPeixe > 50:
    excesso = pesoDoPeixe - 50
    multa = excesso * 4.00
    print("O peixe excedeu:", excesso, "quilo"+
          "\nE a multa é de:", multa, "reais")
else:
    print("O peixe está dentro da regulamento")

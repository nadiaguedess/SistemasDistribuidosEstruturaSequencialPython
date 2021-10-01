metrosUsuario = float(input("Digite a quantidade de metros quadrados a serem pintados:"))

metrosTinta = metrosUsuario / 3
lataTinta = 18
valorLata = 80
quantidadeLata = round(metrosTinta / lataTinta)
valorFinal = round(valorLata * quantidadeLata)
print("para pintar", metrosUsuario, "m² necessita de", quantidadeLata, "latas\nvalor de:", valorFinal, "R$")

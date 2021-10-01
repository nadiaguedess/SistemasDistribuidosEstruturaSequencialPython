turno = input("Digite o seu turno (M - Matutino, V - Vespentino ou N - Noturno):\n")

if(turno.lower() == "m"):
    print("Bom dia!!")
elif(turno.lower() == "v"):
    print("Boa tarde")
elif(turno.lower() == "n"):
    print("Boa noite")
else:
    print("Erro!")
salarioHora = float(input("Digite quantos você ganha por hora:"))
horasTrabalhadas = int(input("Digite quantas horas você trabalhou no mês:"))

salarioBruto = salarioHora * horasTrabalhadas
print("Seu salário bruto é:", salarioBruto)

ir = salarioBruto * 0.11
print("IR (11%):", ir)
inss = salarioBruto * 0.08
print("INSS (8%):", inss)
sindicato = salarioBruto * 0.05
print("Sindicato (5%):", sindicato)
salarioLiquido = salarioBruto - (ir+inss+sindicato)
print("Seu salrio liquido é: ", salarioLiquido)


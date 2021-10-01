mB = float(input("Digite o tamanho do arquivo:"))
mBPS = float(input("Digite a velocidade da internet:"))
operacao = round((mB / (mBPS / 8)) / 60,2)
print("o tempo aproximado de download do arquivo é de:", operacao,"minutos")

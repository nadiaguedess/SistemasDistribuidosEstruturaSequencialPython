
#1)
def atividade1():
    print('Alo mundo!')

#2)
def atividade2():
    print('Por favor digite dois números para que o programa realize a soma dos mesmos.')
    numeroUm = int(input('Digite o primeiro número: '))
    numeroDois = int(input('Digite o segundo número: '))
    soma = numeroUm + numeroDois
    print('A soma de', numeroUm , " + " , numeroDois , " = " , soma)

#9)
def atividade9():
    tempF = int(input('Por favor digite a temperatura em Farenheit: '))
    convertTemp = (5 * (tempF - 32) / 9)
    print('A temperatura ', tempF , "°F em graus celsius é:" , round(convertTemp, 2) , "°C")

def numeroAtividadeValidar(numero):
    if numero == 1:    
        atividade1()
        desejaTestarOutra()
    elif numero == 2:
        atividade2()
        desejaTestarOutra()
    else:
        atividade9()
        desejaTestarOutra()

def desejaTestarOutra():
    desejaValidar = input('Deseja validar outra atividade (S/N): ')
    if desejaValidar != 'S' and desejaValidar != 'N':
        print('Valor informado inválido, o valor deve ser S ou N!')
        desejaTestarOutra()
    elif desejaValidar == 'S':
        numAtiv = int(input('Digite o número da atividade que deseja validar: '))
        numeroAtividadeValidar(numAtiv)  
    else:
        print('Fim!')

numeroAtividade = int(input('Por favor digite o número da atividade que deseja validar: '))

if numeroAtividade == 1:
    atividade1()
    desejaTestarOutra()
elif numeroAtividade == 2:
    atividade2()
    desejaTestarOutra()
else:
    atividade9()
    desejaTestarOutra()


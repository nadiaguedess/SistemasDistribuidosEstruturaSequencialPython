#   1)
def Atividade1():
    nota = int(input('Digite uma nota entre zero e dez: '))
    while  nota < 0 or nota > 10:
        print('Digite um nota válida, entre zero e dez.')
        nota = int(input('Digite o primeiro número: '))
    else:
        print('Parabéns, você digitou uma nota válida!')


#   2)
def Atividade2():
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    while  usuario == senha:
        print('ERRO: A senha não pode ser igual ao usuário!')
        usuario = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
    else:
        print('Parabéns, você digitou o usuário e senha válidos!')


#   3)
def Atividade3():
    mensagem = ""
    nome = input('Digite um nome com no mínimo 4 caracteres: ')
    while  len(nome) < 4:
        print('ERRO: O nome digitado é inválido!')
        nome = input('Digite um nome com no mínimo 3 caracteres: ')
    else:
        mensagem = "Parabéns você digitou o nome corretamente! \n"

    idade = int(input('Digite uma idade entre 0 e 150: '))
    while  idade  < 0 or idade > 150:
        print('ERRO: Idade inválida!')
        idade = int(input('Digite uma idade entre 0 e 150: '))
    else:
        mensagem = mensagem + "Parabéns você digitou a idade corretamente! \n"
    
    salario = float(input('Digite um salário maior que zero: '))
    while  salario <= 0:
        print('ERRO: Salário inválido!')
        salario = float(input('Digite um salário maior que zero: '))
    else:
        mensagem = mensagem + 'Parabéns, você digitou um salário válido! \n'

    
    sexo = input('Digite f ou m para representar um sexo: ')
    while  sexo != 'f'  and 'm':
        print('ERRO: Você digitou um valor inválido!')
        sexo = input('Digite f ou m para representar um sexo: ')
    else:
        mensagem = mensagem + 'Parabéns, você digitou o valor correto para representar o sexo! \n'

    estados_civis_array = ['s', 'c','v','d']
    estavocivil = input('Digite s, c, v ou d para representar o estado civil: ')
    while estavocivil not in estados_civis_array:
        print('ERRO: Você digitou um valor inválido para o estado civil!')
        estavocivil = input('Digite s, c, v ou d para representar o estado civil: ')
    else:
        mensagem = mensagem + 'Parabéns, você digitou um valor válido para o estado civil! \n'

    print(mensagem)


def numeroAtividadeValidar(numero):
    if numero == 1:    
        Atividade1()
        desejaTestarOutra()
    elif numero == 2:
        Atividade2()
        desejaTestarOutra()
    else:
        Atividade3()
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

numeroAtividade = int(input('Por favor digite o número da atividade que deseja validar (números válidos: 1, 2 ou 3): '))

if numeroAtividade == 1:
    Atividade1()
    desejaTestarOutra()
elif numeroAtividade == 2:
    Atividade2()
    desejaTestarOutra()
else:
    Atividade3()
    desejaTestarOutra()


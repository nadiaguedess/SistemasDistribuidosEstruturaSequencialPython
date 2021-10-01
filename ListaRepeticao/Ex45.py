gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
aluno = []
notasDeTodosOsAlunos = []
totalSistema = 0
mediaTurmaCal = []
nota = 0
y = 0
outroAluno = 'sim'

while outroAluno.lower() == "sim":

    for x in range(1, 11):
        print('Digite sua resposta da', x, 'º questão:')
        respsotaAluno = input()
        aluno += [respsotaAluno.upper()]

    while y < 10:
        if aluno[y] == gabarito[y]:
            nota += 1
        y += 1

    print("Voce acertou", nota, "de 10")

    notasDeTodosOsAlunos += [nota]
    mediaTurmaCal += [nota]
    totalSistema += 1
    outroAluno = input("Outro vai ultilizar o sisitema?(sim/não):\n")

    aluno = []
    nota = 0
    y = 0

mediaTurmaCal2 = sum(mediaTurmaCal) / totalSistema

print("O maior acerto foi", max(notasDeTodosOsAlunos))
print("A menor acerto foi", min(notasDeTodosOsAlunos))
print("Total de alunos que ultizou o sistema", totalSistema)
print("Media da turma", mediaTurmaCal2)

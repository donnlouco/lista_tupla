#  47. Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela nota em ordem decrescente.

aluno = []
tupla = ()
while True:
    nom = input('Digite o nome do aluno: (Digite 0 para SAIR) ')
    nota = float(input(f'Digite a nota do aluno {nom}: (Digite 0 para SAIR) '))
    if nom and nota == 0:
        break
    aluno.append = ((nom, nota))
    tupla = sorted(aluno)
    
print(tupla)

# alunos = []
# alunos_c = 0

# # Solicita dados de 5 alunos, por exemplo
# for i in range(5):
#     nome = input(f"Digite o nome do {i+1}º aluno: ")
#     nota = float(input(f"Digite a nota de {nome}: "))
#     alunos.append((nome, nota))
#     alunos_c = sorted(alunos)
    
# print(alunos_c)
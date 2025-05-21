# 35. Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas com mais de 18 anos.

lista = []

while True:
    nome = input ('Digite um nome:(Digite 0 para sair) ')
    idade = int (input ('Digite a idade dessa pessoa: (Digite 0 para sair)  '))
    if nome and idade == 0:
        break
    tupla = (nome, idade)
    lista.append(tupla)

for nome, idade in lista:
    if idade > 18:
        print(nome, idade)



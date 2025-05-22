# 2. Solicite ao usuario 5 nomes e armazene em uma lista. Depois, imprima cada nome em uma linha.

nomes = []

for i in range (5):
    a = input('Digite 5 nomes ')
    nomes.append (a)
    
for j in nomes:
    print( j )
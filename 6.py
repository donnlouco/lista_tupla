# Solicite 5 numeros ao usuario e armazene em uma lista. Em seguida, imprima o maior e o menor numero

numero = []

for i in range (5):
    x = int (input ('Digite 5 valores '))
    numero.append(x)
    numero.sort()
    
print(numero[-1])
print(numero[0])
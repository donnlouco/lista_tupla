# 13. Crie uma lista com os numeros de 1 a 10 usando range() e imprima somente os pares.


numeros = []
for lista in range (1, 11):
    numeros.append(lista)
    
for par in numeros:
    if par % 2 ==0:
        print (par)
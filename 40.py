# 40. Implemente uma funcao que conte quantas vezes um valor aparece em uma lista. 

lista_numeros = [3, 1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10]
contador = 0

for i in lista_numeros:
    if i == 3:
        contador += 1
        
print(f'O numero 3 apareceu {contador} vezes na lista ')
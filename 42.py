# 42. Dada uma lista de inteiros, crie uma funcao que identifique os numeros que aparecem mais de uma vez e quantas vezes cada um aparece.

lista1 = [1, 2, 3, 2, 4, 1, 3, 5, 6, 7, 8, 2, 1, 9, 2, 10]

quantide = {}

for i in lista1:
    if i in quantide:
        quantide[i] += 1
    else:
        quantide[i] = 1

for i, j in quantide.items():
    print(f'o numero {i} aparece {j}')
    

for i in set(lista1):  # Para cada número único
    contagem = lista1.count(i)
    if contagem > 1:
        print(f"Número {i} aparece {contagem} vezes.")
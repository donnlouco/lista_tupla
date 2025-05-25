# 42. Dada uma lista de inteiros, crie uma funcao que identifique os numeros que aparecem mais de uma vez e quantas vezes cada um aparece.

lista1 = [1, 2, 3, 2, 4, 1, 3, 5, 6, 7, 8, 2, 1, 9, 2, 10]
lista2 = list(set(lista1))
fora = []

for i in lista1:
    for j in lista2:
        if i == j:
            fora.append(i)
print(fora)
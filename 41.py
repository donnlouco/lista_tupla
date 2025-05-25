# 41. Crie uma funcao que compare duas listas e retorne os elementos que estao em ambas (intersecao).

lista1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lista2 = set([2, 4, 6, 7, 8])
intersecao = lista1 and lista2


        
print(intersecao)



lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [2, 4, 6, 7, 8]
intersecao = []

for i in lista1:
    for j in lista2:
        if i == j:
            intersecao.append(i)

print(intersecao)
# 31. Crie uma funcao que verifique se uma lista esta ordenada.
lista_numeros = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_ordenada = sorted(lista_numeros)

if lista_numeros == lista_ordenada:
    print('A lista esta ordenada ')
else:
    print('A lista nao esta ordenada ')
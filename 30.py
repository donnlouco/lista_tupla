# 30. Dada uma lista de strings, crie uma nova lista com o tamanho (numero de caracteres)de cada string.

lista_string = ['lista', 'compra', 'arrozaao', 'uva', 'comidassa']


lista_num = []
for j in lista_string:
    num_string = len(j)
    lista_num.append(num_string)
print(lista_num)
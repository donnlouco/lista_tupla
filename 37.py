#  37. Crie uma lista de palavras e remova as que tiverem menos de 4 letras.

lista_string = ['lista', 'compra', 'arrozaao', 'casaoo', 'uva', 'comidassa', 'ana', 'aba']

for i in lista_string[:]: #[:] percorre a lista de tras para frente para evitar pular
    #Quando removemos elementos de uma lista enquanto a percorremos, os índices mudam, o que pode causar erros ou pular elementos.
    if len(i) > 4:
        lista_string.remove(i)
        
print(lista_string)

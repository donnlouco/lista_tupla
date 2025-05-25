#  38. Implemente uma funcao que receba uma lista e retorne os elementos na ordem inversa.
inversa = []
lista_string = ['lista', 'compra', 'arrozaao', 'casaoo', 'uva', 'comidassa', 'ana', 'aba']

for i in lista_string[::-1]: #[::-1]: cria uma nova lista invertida.
    inversa.append(i)

        # OU
        
for i in reversed(lista_string): #gera um iterador invertido,
    inversa.append(i)
    
    
print(inversa)
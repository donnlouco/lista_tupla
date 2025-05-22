#  23. Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem.
# ate poderia usar SET, porem ele nao mantem a ORDEM ORIGINAL


lista_nomes = ['vini', 'ana', 'vini', 'cecilia', 'ana', 'rafaela', 'cecilia', 'rafael', 'ana']
nomes_sem_duplicatas = list(dict.fromkeys(lista_nomes))# O método dict.fromkeys() cria um dicionário com as chaves sendo os elementos da lista 
# Em seguida, o método list() converte as chaves do dicionário de volta em uma lista.

print(nomes_sem_duplicatas)


nomes_sem_duplicatas = list(set(lista_nomes))

print(nomes_sem_duplicatas)
# 10. Dada uma lista de palavras, junte todas elas em uma string separada por v´ırgulas.

lista = ['gabi', 'camamoto', 'larissa', 'mari', 'malu', 'luma']
soma = ''
for palavra in lista:
    if lista[-1]:
        soma += (palavra + ',')
    else:
        soma += (palavra + ',')
    
print(soma)

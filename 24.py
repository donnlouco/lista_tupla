
#  24. Separe uma lista de numeros em duas: uma com pares e outra com ımpares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []

for impar in lista_numeros:
    if impar % 2 != 0:
        lista_impar.append(impar)

for par in lista_numeros:
    if par % 2 == 0:
        lista_par.append(par)
        
print(f'Lista de pares{lista_par} e lista de impares {lista_impar}')
#  21. Solicite ao usuario 10 numeros, armazene em uma lista e remova todos os numeros pares usando remove.

lista_num = []

for numeros in range(10):
    num = int(input('Digite 10 numeros (1 numero por vez): '))
    lista_num.append(num)
    
    
for par in lista_num:
    if par % 2 ==0:
        lista_num.remove(par)
            
print(lista_num)
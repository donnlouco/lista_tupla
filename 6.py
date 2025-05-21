lista = []

for i in range (5):
    num = int(input('sei la '))
    lista.append(num)

    lista.sort()

print(lista[-1], lista[0])
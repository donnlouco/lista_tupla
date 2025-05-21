# 34. Faca um programa que leia numeros do usuario ate digitar -1. Depois, imprima a media.

contador = 0
numerador = 0
while True:
    numero = int(input('Digite numeros: (digite -1 para encerrar ) '))
    if numero != -1:
        contador += 1
        numerador += numero
    else:
        break

print(f'A media é: {(numerador/contador)}')


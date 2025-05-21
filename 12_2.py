

i = 0
contador = 0
while i < 5:
    numero = int(input('Digite 5 valores: '))
    if numero > 10:
        print('O valor foi aceito')
        i +=1
        contador +=1
    else:
        print('O valor nao foi aceito, tente novamente')
        contador +=1
print(f'Voce passou no testezinho, com {contador} tentativas')
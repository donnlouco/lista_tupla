# 12. Leia 5 numeros do usuario e verifique se cada um deles e maior que 10.


for i in range(5):
    numeros = int(input('Digite 5 numeros: '))
    if numeros > 10:
        print('O numero foi aceito')
    else:
        print('O numero nao foi aceito')

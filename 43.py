# 43. Implemente um sistema que simule um carrinho de compras: adicao, remocao e total de itens com precos.

carrinho = {}
soma = 0
from random import randint

while True:
    nome_item = input('informe o nome do item que deseja: ').upper()
    if nome_item == "SAIR":
        break
    p = randint(0, 100)
    preco_item = input(f'O preco do item {nome_item} e R${p}, deseja colocar em seu carrinho? (SIM ou NAO): ').upper()
    if preco_item == 'SIM':
        carrinho[nome_item] = {'preco': p}
    print('Digite sair para sair')
    
for j, i in carrinho.items():
    soma += i['preco']
    print(j, i)
print(soma)

# for i, j in carrinho.items():
#     remover = input(f'Deseja remover o {i}? (NAO para passar) ').upper()
#     if remover == 'NAO' or 'N':
#         pass
#     else:
#         del carrinho[i]

# print(f'O valor total foi R$ {valor}')  
# print(f'Seus itens foram: {carrinho}')


# from random import randint
# carrinho = []
# final = 0
# while True:
#     itens = []
#     preco = []
#     nome_item = input('informe o nome do item que deseja: ').upper()
#     if nome_item == "SAIR":
#         break
#     p = randint(0, 100)
#     preco_item = input(f'O preco do item {nome_item} e R${p}, deseja colocar em seu carrinho? (SIM ou NAO): ').upper()
#     if preco_item == 'SIM':
#         itens.append(nome_item)
#         preco.append(p)
#     carrinho.append(list(zip(itens, preco)))
#     print('Digite sair para sair')
    

# print(carrinho)
# for i in carrinho:
#     remover = input(f'Deseja remover o {i}? (NAO para passar) ').upper()
#     if remover == 'SIM' or 'S':
#         carrinho.remove(i)
#     else:
#         pass


# print(f'Seus itens foram: {carrinho}')
# print(f'Seus itens foram: {sum(i for j, i in carrinho)}')


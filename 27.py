#  27. Simule uma pilha usando append e pop. Mostre a pilha a cada operacao.

pilha = [1, 2, 3, 4, 5, 6, 7]
while True:
    numero_usu = int(input('Digite um valor (quando quiser sair, digite "000"): '))
    if numero_usu == 000:
        break
    pilha.append(numero_usu)
    elemento_removido = pilha.pop(0)
    print(pilha)
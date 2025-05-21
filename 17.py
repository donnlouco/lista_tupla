# 17. Crie uma lista com 5 numeros e calcule a media usando laco for.

numeros = [1, 2, 3, 4, 5]
var = sum(numeros) / len(numeros)
print(var)

media = 0
for soma in numeros:
    media += soma
    mediaf = media / (len(numeros))
print(mediaf)
# 33. Crie uma lista com numeros de 1 a 100 e filtre os multiplos de 3.

lista100 = list(range(1, 101))

for triplo in lista100:
    if triplo % 3 == 0:
        
        print(triplo)
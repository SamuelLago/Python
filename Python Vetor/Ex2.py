vet = []
soma = 0
cont = 0

n = int(input('Digite quantos números você irá utilizar: '))

for i in range (n):
    vet.append(int(input(f"Digite o {i + 1}° número")))
    if(vet[i] % 2 == 0):
        soma += vet[i]
        cont += 1

media = soma / cont

print(media)


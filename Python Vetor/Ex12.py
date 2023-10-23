vet = []
mediacima = 0
mediabaixo = 0
soma = 0
contb = 0
conta = 0

for i in range(50):
    vet.append(int(input(f"Digite a nota da {i + 1}° prova: ")))
    soma += vet[i]

media = soma / 50
mediacima = media * 1.10
mediabaixo = media * 0.9

for i in range(50):
    if(mediabaixo > vet[i]):
        contb += 1
    if(mediacima < vet[i]):
        conta += 1

print(f"10% acima da média: {conta}")
print(f"10% abaixo da média: {contb}")

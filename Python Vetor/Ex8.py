vet = []
for i in range(20):
    vet.append(int(input(f"Digite o {i + 1}° número: ")))

Maior = vet[0]
Menor = vet[0]

for i in range(20):
    if(Maior < vet[i]):
        Maior = vet[i]
    if(Menor > vet[i]):
        Menor = vet[i]

print(f"O maior número é: {Maior} e o menor número é: {Menor}")
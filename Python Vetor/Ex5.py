vet1 = []
vet2 = []
vet = 0

for i in range(50):
    vet1.append(int(input(f"Digite o {i + 1}° número 1 vetor: ")))

for i in range(50):
    vet2.append(int(input(f"Digite o {i + 1}° número 2 vetor: ")))

for i in range(50):
    vet += vet1[i]
    vet += vet2[i]

print(vet)
    
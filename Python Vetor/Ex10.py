vet = []
vet2 = []

for i in range(30):
    vet.append(int(input(f"Digite o {i + 1}° número: ")))

for i in range(29, -1, -1):
    vet2.append(vet[i])

for i in range(30):
    print(vet2[i])



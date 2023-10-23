vet = []
vet2 = []
for i in range(30): 
    vet.append(int(input(f"Digite o {i + 1}° número: ")))

for i in range(30):
    if(i % 2 == 0):
        vet2.append(vet[i] * 2)
    if(i % 2 != 0):
        vet2.append(vet[i] * 3)
for i in range(30):
    print(vet2[i])
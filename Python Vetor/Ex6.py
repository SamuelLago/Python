vet = []

for i in range (100):
    vet.append(int(input(f"Digite o {i + 1}° número: ")))

for i in range(100):
    if(vet[i] % 2 == 0):
        vet[i] = 0
    if(vet[i] % 2 != 0):
        vet[i] = 1
        
for i in range(100):
    print(vet[i])
vet  = []
vetpar = []
vetimpar = []
cont = 0
cont1 = 0
for i in range(20):
    vet.append(int(input(f"Digite o {i + 1}° número: ")))

for i in range(20):
    if(vet[i] % 2 == 0):
        vetpar.append(vet[i])
        cont += 1
    if(vet[i] % 2 != 0):
        vetimpar.append(vet[i])
        cont1 += 1

for i in range(cont1):
    print(f"Números impares: {vetimpar[i]}")

for i in range(cont):
    print(f"Números pares: {vetpar[i]}")
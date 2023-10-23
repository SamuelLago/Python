vet = []
soma = 0
cont = 0

n = int(input("Digite a quantidade de alunos: "))

for i in range(n):
    vet.append(int(input("Digite a nota dos alunos: ")))
    soma += vet[i]
    cont += 1

media = soma / cont

for i in range(n):
    if(media < vet[i]):
        cont += 1

print(f"O número de aprovados é: {cont}")
Num  = int(input(f"Digite o tamanho do febonacci: "))
num1 = 1
num2 = 1
num3 = 0
vet = []

for i in range(Num):
    num3 = num1 + num2
    vet.append(num3)
    num2 = num1
    num1 = num3

for i in range(Num):
    print(vet[i])
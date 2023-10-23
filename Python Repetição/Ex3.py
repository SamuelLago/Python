soma = 0
cont = 0
for info in range(10):
    info = int(input("Digite 10 números: "))
    if info % 2 == 0:
        soma += info
        cont += 1

result = soma / cont
print(f"A média de pares é: {result}")
num = 1
soma = 0
cont = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0 and num != 0:
        soma += num
        cont += 1

result = soma / cont
print(f"A média de pares é: {result}")

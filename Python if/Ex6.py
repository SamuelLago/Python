num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 < num2:
    dist = num2 - num1
    print(f"Distancia entre os pontos é: {dist}")
elif num1 > num2:
    dist = num1 - num2
    print(f"Distancia entre os pontos é: {dist}")
else:
    print("Pontos iguais")
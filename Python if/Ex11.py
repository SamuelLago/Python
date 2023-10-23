num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num1 == num2 == num3:
    print(f"É um triângulo equilátero")

elif num1 <= num2 + num3 and num2 <= num3 + num1 and num3 <= num1 + num2:
    if num1 == num2 or num2 == num3 or num3 == num1:
        print(f"É um triângulo isóceles")
    else:
        print(f"É um triângulo escaleno")
else:
    print("Número inválido")

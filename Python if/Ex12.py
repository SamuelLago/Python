num1 = float(input("Digite sua altura(metros): "))
sexo = input("Digite o seu sexo: ")

if sexo == "m" or sexo == "masculino":
    peso = (72.7 * num1) - 58
    input(f"Seu peso ideal é: {peso}")
elif sexo == "f" or sexo == "feminino":
    peso = (62.1 * num1) - 44.7
    input(f"Seu peso ideal é: {peso}")
else:
    input(f"Sexo inválido")
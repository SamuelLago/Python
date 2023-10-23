num1 = int(input("Digite um número com 3 digitos: "))

if num1 > 99 and num1 < 1000:
    
    centena = num1 // 100
    dezena = (num1 - (centena * 100)) // 10
    unidade = (num1 - (centena * 100) - (dezena * 10))

    print(f"{unidade}{dezena}{centena}")

else:
    print(f"Número Inválido")

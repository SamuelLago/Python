comb = int(input("Digite qual combustível irá escolher: \n1- G\n2- A \n"))
litros = int(input("Digite a quantidade de combustivel: "))

if  litros > 0 and litros < 20:
    if comb == 2:
        v = (2.10 * 0.97) * litros
        print(f"Preço a pagar: {v}")
    elif comb == 1:
        v = (3.30 * 0.96) * litros
        print(f"Preço a pagar: {v}")
    else:
        print("Escolha inválida")

elif litros > 20:
    if comb == 2:
        v = (2.10 * 0.96) * litros
        print(f"Preço a pagar: {v}")
    elif comb == 1:
        v = (3.30 * 0.94) * litros
        print(f"Valor a pagar: {v}")
    else:
        print("Escolha inválida")
else:
    print("Valor inválido")


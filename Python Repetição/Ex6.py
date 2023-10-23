vinho = ""
while vinho != "F":
    vinho = input("Escolha o vinho:\n1-Tinto(T)\n2-Branco(B)\n3-Rosê(R)\n4-Sair(F)\n")
    if vinho == "T":
        vinhoT = int(input("Digite a quantidade de vinhos tintos: "))
    elif vinho == "B":
        vinhoB = int(input("Digite a quantidade de vinhos brancos: "))
    elif vinho == "R":
        vinhoR = int(input("Digite a quantidade de vinhos rosê: "))
    elif vinho != "T" or "F" or "B" or "R":
        ("Escolha inválida!")

TotalVinhos = vinhoT + vinhoB + vinhoR
porcentT = (vinhoT / TotalVinhos) * 100
porcentB = (vinhoB / TotalVinhos) * 100
porcentR = (vinhoR / TotalVinhos) * 100
print(f"Vinho Tinto: {porcentT:.2f}%, Vinho Branco: {porcentB:.2f}%, Vinho Rosê: {porcentR:.2f}%")
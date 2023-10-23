achar = int(input("Digite um número para seu amigo adivinhar: "))
num = None
while num != achar:
    num = int(input("Digite o número para adivinhar: "))
    if num > achar:
        print("Mais baixo")
    elif num < achar:
        print("Mais alto")
    else:
        print(f"Párabens você acertou o número é {achar}")
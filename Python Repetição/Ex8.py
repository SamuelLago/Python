num1 = int(input("Digite um número para a tabuada: "))

while num1 != -1:
    for i in range(10):
        print(f"{num1} x {i} = {num1 * i}")
        
    num1 = int(input("Digite um número para a tabuada ou -1 para sair: "))
    i = 1
    
print("Saindo...")
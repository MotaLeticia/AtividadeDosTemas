valorInicial = int(input("Digite o valor inicial: "))
valorFinal = int(input("Digite o valor final: "))

# laço de repetição
while valorFinal < valorInicial:
    print("Escreva um número que o valor iicial seja menor que o valor final")
    valorInicial = int(input("Digite o valor inicial: "))
    valorFinal = int(input("Digite o valor final: "))

for i in range(valorInicial,valorFinal + 1):
    print(i)
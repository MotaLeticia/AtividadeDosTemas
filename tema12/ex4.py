total = 0
for _ in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        total += numero
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print("A soma dos números lidos é:", total)



def eh_primo(numero):
    if numero <= 1:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    # Percorre apenas os números ímpares
    for i in range(3, numero // 2 + 1, 2):
        if numero % i == 0:
            return False

    return True

try:
    numero = int(input("Digite um número inteiro: "))
    if eh_primo(numero):
        print(str(numero) + " é um número primo!")
    else:
        print(str(numero) + " não é um número primo.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
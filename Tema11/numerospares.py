def soma_numeros_pares(ate_numero):
    soma = 0
    for num in range(1, ate_numero + 1):
        if num % 2 == 0:
            soma += num
    return soma

try:
    numero_fornecido = int(input("Digite um número inteiro: "))
    if numero_fornecido < 1:
        print("Por favor, digite um número maior ou igual a 1.")
    else:
        resultado = soma_numeros_pares(numero_fornecido)
        print(str(resultado)+ "é a soma dos números pares até " + str(numero_fornecido) + ".")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
    
    
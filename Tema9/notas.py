def calcular_notas(valor):
    notas_50 = valor // 50
    valor = valor % 50
    
    notas_10 = valor // 10
    valor = valor % 10
    
    notas_1 = valor // 1
    
    return notas_50, notas_10, notas_1

# Entrada do usuário
valor = int(input("Digite o valor da conta: R$ "))

# Calcula a quantidade de notas
notas_50, notas_10, notas_1 = calcular_notas(valor)

# Exibe os resultados
print("Notas de 50: ", notas_50)
print("Notas de 10: ", notas_10)
print("Notas de 1: ", notas_1)

def calcular_diferenca(valores):
    maior = max(valores)
    menor = min(valores)
    diferenca = maior - menor
    return diferenca

# Entrada do usuário
valores = []
n = int(input("Quantos valores você deseja inserir? "))

for i in range(n):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

# Calcula a diferença
diferenca = calcular_diferenca(valores)

# Exibe o resultado
print("A diferença entre o maior e o menor valor é:", diferenca)

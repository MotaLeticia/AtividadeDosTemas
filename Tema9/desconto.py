def calcular_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_com_desconto = preco_original - valor_desconto
    return valor_desconto, preco_com_desconto

# Entrada do usuário
preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o desconto e o preço com desconto
valor_desconto, preco_com_desconto = calcular_desconto(preco_original, percentual_desconto)

# Exibe os resultados
print("Valor do desconto: R$ " + str(round(valor_desconto, 2)))
print("Preço com desconto: R$ " + str(round(preco_com_desconto, 2)))


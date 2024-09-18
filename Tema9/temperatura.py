def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = ((celsius * 9) / 5) + 32
    return fahrenheit

# Entrada do usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit
fahrenheit = converter_celsius_para_fahrenheit(celsius)

# Exibe o resultado
print("A temperatura em Fahrenheit é: " + str(fahrenheit))

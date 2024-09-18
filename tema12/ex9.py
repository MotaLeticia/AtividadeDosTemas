def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Peso (Kg): "))
altura = float(input("Altura (M): "))
imc = calcular_imc(peso, altura)

print("Seu IMC é:", imc)


if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")

#Recebimento de valores
numero = int(input("Digite um valor inteiro: "))

#Conversão de valor inteiro para string
numeroInvertido = str(numero)[::-1]



#Verificando o Palindromo

print("")

if numeroInvertido == str(numero):
    
    print(str(numero)+ "O número é um palindromo" + str(numeroInvertido) + ".")

else:
    print(str(numero)+ "O número não é palindromo")
    
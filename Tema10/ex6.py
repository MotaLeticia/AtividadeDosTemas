def cifra_de_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for caractere in mensagem:
        if caractere.isalpha():
            deslocamento = 65 if caractere.isupper() else 97
            mensagem_criptografada += chr((ord(caractere) - deslocamento + chave) % 26 + deslocamento)
        else:
            mensagem_criptografada += caractere
    return mensagem_criptografada

# Entrada do usuário
mensagem = input("Digite a mensagem a ser criptografada: ")
chave = int(input("Digite a chave de criptografia (um número inteiro): "))

# Criptografa a mensagem
mensagem_criptografada = cifra_de_cesar(mensagem, chave)

# Exibe a mensagem criptografada
print("Mensagem criptografada:", mensagem_criptografada)

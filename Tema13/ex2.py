def validar_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    else:
        return False

# Entrada do usuário
email = input("Digite o endereço de e-mail: ")

# Valida o e-mail
if validar_email(email):
    print("Endereço de e-mail válido.")
else:
    print("Endereço de e-mail inválido.")

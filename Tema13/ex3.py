import re

def validar_nome(nome):
    # Verifica se o nome contém apenas letras e espaços
    if re.match("^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", nome):
        return True
    else:
        return False

# Exemplo de uso
nome = input("Digite seu nome: ")
if validar_nome(nome):
    print("Nome válido!")
else:
    print("Nome inválido. Por favor, use apenas letras e espaços.")

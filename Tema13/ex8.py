def validar_campo_vazio(campo):
    return len(campo.strip()) > 0

# Exemplo de uso
campo = input("Digite algo: ")
if validar_campo_vazio(campo):
    print("Campo preenchido!")
else:
    print("Campo vazio.")

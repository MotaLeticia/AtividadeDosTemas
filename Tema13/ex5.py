def validar_rg(rg):
    rg_numerico = ""
    for char in rg:
        if char.isdigit():
            rg_numerico += char
    return len(rg_numerico) == 9

# Exemplo de uso
rg = input("Digite seu RG: ")
if validar_rg(rg):
    print("RG válido!")
else:
    print("RG inválido.")

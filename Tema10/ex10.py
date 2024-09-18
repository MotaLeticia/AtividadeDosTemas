# Criação do dicionário para o animal de estimação
animal_estimacao = {
    "nome": "Bobby",
    "tipo": "Gato",
    "idade": 3
}

# Exibição das informações do dicionário
print("Informações do animal de estimação:")
for chave, valor in animal_estimacao.items():
    print("{}: {}".format(chave.capitalize(), valor))

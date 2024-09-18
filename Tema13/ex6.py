def validar_data(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        return 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0
    except ValueError:
        return False

# Exemplo de uso
data = input("Digite uma data (dd/mm/aaaa): ")
if validar_data(data):
    print("Data válida!")
else:
    print("Data inválida.")

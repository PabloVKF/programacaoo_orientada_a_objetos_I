# Tema perfeito da questão!
number_of_values: int = int(input())
budget: int = 0
expendinture: int = 0

# O for certifica que tera um campo para cada input
for number in range(number_of_values):
    entry: list = input().split()
    type_entry: str = entry[0]
    value: int = int(entry[1])

    # Já esse if, garante que o valor sejá acrescentado na variavel certa
    if type_entry == "V":
        budget += value
    elif type_entry == "G":
        expendinture += value

# Esse if verifica se devemos continuar lutando por nossos direitos
if expendinture > budget:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")

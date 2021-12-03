# Tanto nesse quanto em outros exercicio vou input().split() e distribuir as variaveis uma a uma.
# Pois mesmo gostando de usar o map(), notei que ele aumenta muito o tempo de processamento.
# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
entry: list = input().split()
wheat: int = int(entry[0])
eggs: int = int(entry[1])
milk: int = int(entry[2])

# Pegando a quantidade de bolos que cada ingrediente consegue suprir
cake_per_wheat: int = wheat // 2
cake_per_eggs: int = eggs // 3
cake_per_milk: int = milk // 5

# min() devolve a menor das qualtidades fornecidas
print(min(cake_per_wheat, cake_per_eggs, cake_per_milk))

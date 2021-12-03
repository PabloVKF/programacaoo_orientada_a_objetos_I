# Tanto nesse quanto em outros exercicio vou input().split() e distribuir as variaveis uma a uma.
# Pois mesmo gostando de usar o map(), notei que ele aumenta muito o tempo de processamento.
# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
entry: list = input().split()
humanos: int = int(entry[0])
elfos: int = int(entry[1])
anoes: int = int(entry[2])
orcs: int = int(entry[3])
wargs: int = int(entry[4])
aguias: int = int(entry[5])

# Poderia não ter criado as variaveis anteriores e jogar direto aqui como int(entry[i]) e fazer o calculo.
# Porem, por legibilidade do código, optei por instanciar cada valor em uma varivel que represente seu significado
good_side: int = humanos + elfos + anoes + aguias
evil_side: int = orcs + wargs

if evil_side > good_side:
    print("Sauron has returned.")
else:
    print("Middle-earth is safe.")

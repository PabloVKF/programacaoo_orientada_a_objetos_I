# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
# Uso o input seguido do int para garantir que a variavel não entre em nenhum calculo como string.
balls: int = int(input())
branches: int = int(input())

# Aqui pego a diferença da bolinha pela metade dos galhos
needed_balls: int = (branches // 2) - balls

# Aqui a de fato a verificação se será necessario mais bolinhas
if needed_balls > 0:
    print(f"Faltam {needed_balls} bolinha(s)")
else:
    print(f"Amelia tem todas bolinhas!")

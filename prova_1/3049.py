# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
base_1: int = int(input())
base_2: int = int(input())

# calculo da metade da area do retangulo
half_of_rectangle_area: float = (160 * 70) / 2

# calculo da area esquerda resultante
left_area = ((base_1 + base_2) / 2) * 70

# Se a area esquerda gerada for maior que a metade da folha, Felix ganhou, do contrario, Marrzia vence
if left_area > half_of_rectangle_area:
    print(1)
elif left_area < half_of_rectangle_area:
    print(2)
elif left_area == half_of_rectangle_area:
    print(0)

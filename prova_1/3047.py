# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
monica_age: int = int(input())
son_age_1: int = int(input())
son_age_2: int = int(input())

# Calculando a idade do terceiro filho
son_age_3: int = monica_age - son_age_1 - son_age_2

# max() devolvera a idade mais alta
print(max(son_age_1, son_age_2, son_age_3))

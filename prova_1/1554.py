# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
import math


number_of_tests: int = int(input())

# Com o numero informado pude usar range e for para criar um lupe N vezes
for number_test in range(number_of_tests):
    # Coletei a quantidade de bolas sem ser a branca e declarei variaveis inportante para o próximo for
    available_balls: int = int(input())
    white_ball: int = 1
    x_white_ball: int = 0
    y_white_ball: int = 0
    # Esses valores são maiores do que o enunciado permite vir como input, logo sem serão substituidos pelo if a seguir
    closest_ball: int = 1000000
    distance_of_closest_ball: float = 1000000.0

    for number_ball in range(available_balls + white_ball):
        ball_coordenates: list = input().split()
        x_ball: int = int(ball_coordenates[0])
        y_ball: int = int(ball_coordenates[1])

        # Caso seja a primeira bola (bola branca, armazena os dados nas variaveis
        if number_ball == 0:
            x_white_ball = x_ball
            y_white_ball = y_ball
        else:
            # Caso não seja a bola branca, verifica a distancia que esta da bola branca por Pitagoras
            leg_x: int = x_white_ball - x_ball
            leg_y: int = y_white_ball - y_ball
            hypotenuse: float = math.sqrt((leg_x ** 2) + (leg_y ** 2))

            # Se estiver mais proximo que a bola anterior, armazena o valor da bola e a distancia
            is_closer: bool = hypotenuse < distance_of_closest_ball
            if is_closer:
                closest_ball = number_ball
                distance_of_closest_ball = hypotenuse

    print(closest_ball)

# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
test_counter: int = 1

while True:
    number_of_matches: int = int(input())

    if number_of_matches == 0:
        break

    corrent_balance = 0
    beginning_of_the_best_period: int = -1
    ending_of_the_best_period: int = -1
    list_of_goals_balance: list = []
    # Esse primeiro for preenche uma lista com o saldo de gols de cada dia do periodo
    for match in range(number_of_matches):
        scoreboard: list = input().split()
        goals_in_favor: int = int(scoreboard[0])
        goals_against: int = int(scoreboard[1])
        goals_balance: int = goals_in_favor - goals_against
        list_of_goals_balance.append(goals_balance)

    # Enquanto esse for passa por essa lista N vezes, verificando qual o intervalo de dias acumula o maior saldo de gols
    # Com intervalos que variam de 1 a N.
    for index in range(len(list_of_goals_balance)):
        counter = 0
        possibilits = index + 1

        for x in range(possibilits):
            start = counter
            end = len(list_of_goals_balance) - index + start

            mean = sum(list_of_goals_balance[start:end])

            if mean > corrent_balance:
                corrent_balance = mean
                beginning_of_the_best_period = start + 1
                ending_of_the_best_period = end

            counter += 1

    if beginning_of_the_best_period < 0:
        print(f"Teste {test_counter}\n"
              f"nenhum\n")
    else:
        print(f"Teste {test_counter}\n"
              f"{beginning_of_the_best_period} {ending_of_the_best_period}\n")
    test_counter += 1

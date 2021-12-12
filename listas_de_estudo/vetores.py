from typing import List


def loop_musical():
    while True:
        musical_notes: int = int(input())
        if not musical_notes:
            break

        musical_loop: list = list(map(int, input().split()))
        peaks: int = 0
        for index, note in enumerate(musical_loop):
            previous_note: int = musical_loop[index-1]
            if index == (len(musical_loop)-1):
                next_note: int = musical_loop[0]
            else:
                next_note: int = musical_loop[index+1]
            is_the_lower_peak: bool = note == min(previous_note, note, next_note)
            is_the_top_peak: bool = note == max(previous_note, note, next_note)

            if is_the_top_peak or is_the_lower_peak:
                peaks += 1
        print(peaks)


def leitura_otica():
    alternatives: list = ["A", "B", "C", "D", "E"]
    while True:
        number_of_questions: int = int(input())
        if not number_of_questions:
            break

        for question in range(number_of_questions):
            answers: list = list(map(int, input().split()))
            result: str = "*"

            for index, answer in enumerate(answers):
                if answer <= 127:
                    if result == "*":
                        result = alternatives[index]
                    else:
                        result = "*"
                        break

            print(result)


def menor_e_posicao():
    len_vector: str = input()
    vector: list = list(map(int, input().split()))

    min_value: int = min(vector)
    index_min_value: int = vector.index(min_value)

    print(f"Menor valor: {min_value}\n"
          f"Posicao: {index_min_value}")


def bilhetes_falsos():
    while True:
        number_of_tickets, number_of_people = map(int, input().split())
        if not number_of_tickets and not number_of_people:
            break

        tickets_numbers: list = list(map(int, input().split()))

        for ticket in range(1, number_of_tickets + 1):
            try:
                tickets_numbers.remove(ticket)
            except ValueError:
                continue

        print(len(set(tickets_numbers)))


def cara_ou_coroa():
    while True:
        number_of_matches: int = int(input())
        if not number_of_matches:
            break

        matches: list = input().split()
        joao_points: int = 0
        maria_points: int = 0
        for round_result in matches:
            joao_won: int = int(round_result)
            if joao_won:
                joao_points += 1
            else:
                maria_points += 1

        print(f"Mary won {maria_points} times and John won {joao_points} times")


def jogo_de_varetas():
    while True:
        number_of_types: int = int(input())
        if not number_of_types:
            break

        rectangle_sides: list = []
        for number in range(number_of_types):
            sticks_width, number_of_sticks = map(int, input().split())
            rectangle_sides.append(number_of_sticks//2)

        number_of_rectangle: int = sum(rectangle_sides)//2
        print(number_of_rectangle)


def mergulho():
    while True:
        try:
            number_of_divers, number_of_returns = map(int, input().split())
            returned_divers: list = list(map(int, input().split()))

            if number_of_divers == number_of_returns:
                print("*")
            else:
                not_returns_numbers: str = ''
                for diver in range(1, number_of_divers + 1):
                    if diver not in returned_divers:
                        not_returns_numbers += str(diver) + ' '

                print(not_returns_numbers)

        except EOFError:
            break


def circuito_bioquimico_digital():
    while True:
        processing_points, mesurements_taken, stick_width = map(int, input().split())
        if not processing_points and not mesurements_taken and not stick_width:
            break

        sample: list = []
        for number in range(mesurements_taken):
            mesurement: list = list(map(int, input().split()))
            sample.append(mesurement)

        number_of_stick: int = 0
        for number in range(processing_points):
            counter_of_ones: int = 0
            for test in sample:
                if test[number]:
                    counter_of_ones += 1
                    if counter_of_ones == stick_width:
                        number_of_stick += 1
                        counter_of_ones = 0
                else:
                    counter_of_ones = 0

        print(number_of_stick)


def detetive_watson():
    while True:
        number_of_suspects: int = int(input())
        if not number_of_suspects:
            break

        suspects: list = list(enumerate(map(int, input().split()), start=1))
        suspects.sort(key=lambda x: x[1])
        print(suspects[-2][0])


def maquina_de_verificacao_automatica():
    conector_1: list = list(map(int, input().split()))
    conector_2: list = list(map(int, input().split()))

    answer: str = "Y"
    for number in range(len(conector_1)):
        not_pluggable: bool = conector_1[number] == conector_2[number]
        if not_pluggable:
            answer = "N"
            break

    print(answer)


def economia_brasileira():
    number_of_participants: int = int(input())
    answers: list = input().split()

    majority_satisfied: bool = answers.count("0") > number_of_participants // 2
    if majority_satisfied:
        print("Y")
    else:
        print("N")


def o_castelo_de_neve_de_sansa():
    number_of_towers, number_of_peak = map(int, input().split())
    sansa_towers: list = list(map(int, input().split()))

    top_peak: int = 0
    lower_peak: int = 0
    for index, tower in enumerate(sansa_towers):
        if index == 0:
            continue
        previous_tower: int = sansa_towers[index - 1]
        if index == (len(sansa_towers) - 1):
            next_tower: int = sansa_towers[-2]
        else:
            next_tower: int = sansa_towers[index + 1]
        is_the_lower_peak: bool = tower == min(previous_tower, tower, next_tower)
        is_the_top_peak: bool = tower == max(previous_tower, tower, next_tower)

        if is_the_top_peak:
            top_peak += 1
        elif is_the_lower_peak:
            lower_peak += 1

    if top_peak == number_of_peak and lower_peak == number_of_peak:
        print("beautiful")
    else:
        print("ugly")


def pula_sapo():
    jump_height, number_of_pipes = map(int, input().split())
    pipe_sequence: list = list(map(int, input().split()))

    game_result: str = 'YOU WIN'
    for index, pipe in enumerate(pipe_sequence):
        if index == 0:
            continue
        previous_pipe: int = pipe_sequence[index - 1]
        cant_jump_over: bool = abs(pipe - previous_pipe) > jump_height

        if cant_jump_over:
            game_result = "GAME OVER"
            break

    print(game_result)


def aeroporto():
    counter_of_tests: int = 1
    while True:
        number_of_airports, number_of_flights = map(int, input().split())
        if not number_of_airports and not number_of_flights:
            break

        airport_traffic: list = [[airport, 0] for airport in range(1, number_of_airports + 1)]
        for flight_number in range(1, number_of_flights + 1):
            departure, arrival = map(int, input().split())
            airport_traffic[departure-1][1] += 1
            airport_traffic[arrival-1][1] += 1

        airport_traffic.sort(reverse=True, key=lambda x: x[1])
        greater_traffic: int = airport_traffic[0][1]

        print(f"Teste {counter_of_tests}")
        for airport, traffic in airport_traffic:
            if traffic == greater_traffic:
                print(f"{airport} ", end="")
            else:
                break
        print("\n")

        counter_of_tests += 1


def maratona():
    number_of_posts, max_distance = map(int, input().split())
    water_posts: list = list(map(int, input().split()))
    end_of_marathon: int = 42195

    water_posts.append(end_of_marathon)
    marathon_result: str = "S"
    for index, distance in enumerate(water_posts):
        if index == 0:
            continue

        previous_post: int = water_posts[index - 1]
        distance_between_posts: int = distance - previous_post

        if distance_between_posts > max_distance:
            marathon_result = "N"
            break

    print(marathon_result)


def pulo_do_sapo():
    number_of_stones, number_of_frogs = map(int, input().split())

    occupation_stones: list = [0 for i in range(number_of_stones)]
    for frog in range(number_of_frogs):
        inicial_place, jump_width = map(int, input().split())
        first_stone: int = inicial_place % jump_width

        for number in range(len(occupation_stones) + 1):
            stone_location: int = first_stone + (number * jump_width)
            if not stone_location:
                continue
            try:
                occupation_stones[stone_location - 1] = 1
            except IndexError:
                break

    for stone in occupation_stones:
        print(stone)


def campo_minado():
    number_of_cells: int = int(input())

    board: list = []
    for number in range(number_of_cells):
        cell: int = int(input())
        board.append(cell)

    for index, cell in enumerate(board):
        if index == 0:
            previous_cell: int = index
        else:
            previous_cell: int = index - 1

        if index == (len(board)-1):
            next_cell: int = index
        else:
            next_cell: int = index + 1

        print(sum(board[previous_cell:(next_cell + 1)]))




if __name__ == "__main__":
    pulo_do_sapo()

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


def circuito_bioquimico_digital(): # Incompleto
    while True:
        processing_points, mesurements_taken, stick_width = map(int, input().split())
        if not processing_points and not mesurements_taken and not stick_width:
            break

        sample: list = []
        for number in range(mesurements_taken):
            mesurement: int = int(input())
            sample.append(mesurement)


def detetive_watson(): # Incompleto
    while True:
        number_of_suspects: int = int(input())
        if not number_of_suspects:
            break

        suspects: list = list(enumerate(map(int, input().split()), start=1))
        suspects.sort(key=lambda x: x[1])
        print(suspects[-2][0])


if __name__ == "__main__":
    detetive_watson()

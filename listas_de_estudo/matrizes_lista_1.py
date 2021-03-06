def linha_na_matriz():
    row: int = int(input())
    operation: str = input()
    matriz: list = []
    for n_row in range(12):
        matriz.append([float(input()) for n_column in range(12)])

    result: float = 0.0
    current_row: list = matriz[row]
    for colulmn in current_row:
        result += colulmn

    if operation == 'S':
        print(result)
    elif operation == 'M':
        print(round(result / 12, 1))


def abaixo_da_diagonal_principal():
    operation: str = input()
    entries_sum: float = 0.0

    houses: int = 0
    for n_row in range(12):
        for n_column in range(12):
            float_entry: float = float(input())
            if n_column < n_row:
                houses += 1
                entries_sum += float_entry

    if operation == 'S':
        print(entries_sum)
    elif operation == 'M':
        average = round(entries_sum / houses, 1)
        print(average)


def acima_da_diagonal_secundaria():
    operation: str = input()
    entries_sum: float = 0.0

    houses: int = 0
    for n_row in range(12):
        for n_column in range(12):
            float_entry: float = float(input())
            limit: int = 11 - n_row
            if n_column < limit:
                houses += 1
                entries_sum += float_entry

    if operation == 'S':
        print(entries_sum)
    elif operation == 'M':
        average = round(entries_sum / houses, 1)
        print(average)


def abaixo_da_diagonal_secundaria():
    operation: str = input()
    entries_sum: float = 0.0

    houses: int = 0
    for n_row in range(12):
        for n_column in range(12):
            float_entry: float = float(input())
            first_limit: int = n_row
            second_limit: int = 11 - n_row
            if (n_column > first_limit) and (n_column < second_limit):
                houses += 1
                entries_sum += float_entry

    if operation == 'S':
        print(round(entries_sum, 1))
    elif operation == 'M':
        average = round(entries_sum / houses, 1)
        print(average)


def area_acima():
    operation: str = input()
    entries_sum: float = 0.0

    houses: int = 0
    for n_row in range(12):
        for n_column in range(12):
            float_entry: float = float(input())
            first_limit: int = n_row
            second_limit: int = 11 - n_row
            if (n_column > first_limit) and (n_column < second_limit):
                houses += 1
                entries_sum += float_entry

    if operation == 'S':
        print(round(entries_sum, 1))
    elif operation == 'M':
        average = round(entries_sum / houses, 1)
        print(average)


def matriz_quadrada_1():
    while True:
        matriz_number: int = int(input())
        if not matriz_number:
            break

        for row in range(matriz_number):
            for column in range(matriz_number):
                result = min(row + 1, column + 1, matriz_number - row, matriz_number - column)
                if column == 0:
                    print(f'{result:3d}', end='')
                else:
                    print(f' {result:3d}', end='')
            print()
        print()


def competicao():
    while True:
        participantes_number, questions_number = map(int, input().split())
        if not participantes_number and not questions_number:
            break

        got_at_least_one: int = 0
        solved_questions: list = [0 for x in range(questions_number)]
        nobody_got_it_all: bool = True
        for participant in range(participantes_number):
            answers = list(map(int, input().split()))
            for index, answer in enumerate(answers):
                if answer == 1:
                    solved_questions[index] += 1
            if not answers.count(0):
                nobody_got_it_all = False
            if answers.count(1):
                got_at_least_one += 1

        all_solved_at_least_once: bool = not bool(solved_questions.count(0))
        at_least_one_solved_by_all: bool = not bool(solved_questions.count(participantes_number))
        all_got_at_least_one: bool = got_at_least_one == participantes_number

        result = [
            nobody_got_it_all,
            all_solved_at_least_once,
            at_least_one_solved_by_all,
            all_got_at_least_one
        ].count(True)

        print(result)


def desafio_de_bino():
    tests_number: int = int(input())
    multiples: list = [2, 3, 4, 5]
    numbers_test: list = list(map(int, input().split()))
    count_multiples: list = [0 for x in range(len(multiples))]
    for number in numbers_test:
        for index, test in enumerate(multiples):
            if number % test == 0:
                count_multiples[index] += 1

    print(f'{count_multiples[0]} Multiplo(s) de 2\n'
          f'{count_multiples[1]} Multiplo(s) de 3\n'
          f'{count_multiples[2]} Multiplo(s) de 4\n'
          f'{count_multiples[3]} Multiplo(s) de 5')


if __name__ == "__main__":
    desafio_de_bino()

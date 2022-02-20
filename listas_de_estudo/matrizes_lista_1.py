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


def matriz_quadrada_1():
    while True:
        matriz_number: int = int(input())
        if not matriz_number:
            break

        for row in range(matriz_number):
            for column in range(matriz_number):
                result = min(row + 1, column + 1, matriz_number - row, matriz_number - column)
                if column == 0:
                    print('%3d' % result, end='')
                else:
                    print(' %3d' % result, end='')
            print()
        print()


def competicao(): # Incompleto
    while True:
        participantes_number, questions_number = map(int, input().split())
        if not participantes_number and not questions_number:
            break

        results: list = []
        nobody_got_it_all: bool = True
        for participant in range(participantes_number):
            answers = list(map(int, input().split()))
            if not answers.count(0):
                nobody_got_it_all = False
            results.append(answers)

        conditions_satisfied: int = 0
        conditions: list = [
            nobody_got_it_all
        ]



if __name__ == "__main__":
    matriz_quadrada_1()

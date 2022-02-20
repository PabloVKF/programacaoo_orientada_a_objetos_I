def matris_quadrada_iii():
    while True:
        matriz_number: int = int(input())
        if not matriz_number:
            break

        len_big_number: int = len(str((2 ** (matriz_number - 1)) * (2 ** (matriz_number - 1))))

        for row in range(matriz_number):
            for column in range(matriz_number):
                result: str = str((2 ** row) * (2 ** column))
                if column == 0:
                    print(' ' * (len_big_number - len(result)) + f'{result}', end='')
                else:
                    print(' ' * (len_big_number - len(result) + 1) + f'{result}', end='')
            print()
        print()


if __name__ == "__main__":
    matris_quadrada_iii()

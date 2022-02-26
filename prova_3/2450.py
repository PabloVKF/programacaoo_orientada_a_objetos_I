"""
IDEIA DE SOLUÇÃO: Construir a matrix já validadando a primeira regra e depois validar a segunda
"""

lenght_matrix, width_matrix = map(int, input().split())
matrix: list = []
its_over: bool = False
its_stairs: bool = True
for row_n in range(lenght_matrix):
    row_values: list = list(map(int, input().split()))
    matrix.append(row_values)
    is_zero_line: bool = row_values.count(0) == width_matrix

    if its_over and not is_zero_line:
        its_stairs = False

    if is_zero_line:
        its_over = True

if its_stairs:
    for index_row, row in enumerate(matrix):
        if its_stairs:
            for index_column, column in enumerate(row):
                if column != 0:
                    total = 0
                    for i in range(index_row, lenght_matrix):
                        total += sum(matrix[i][0:index_column + 1])
                    if total != column:
                        its_stairs = False
                    break
        else:
            break

if its_stairs:
    print('S')
else:
    print('N')


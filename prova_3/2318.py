matrix: list = []
for number in range(3):
    entry: list = list(map(int, input().split()))
    matrix.append(entry)

coordinate_zeros: list = []
for row in matrix:
    for column, number in enumerate(row):
        if not number:
            coordinate_zeros.append([row, column])
total_incomplet_line: int = 0
total_complet_line: int = 0
for row in matrix:
    if 0 not in row:
        total_complet_line = sum(row)
        break
    else:
        total_incomplet_line = sum(row)
        coordinate_zeros.append()

if not total_complet_line:
    transposed_matrix = list(zip(matrix))
    for row in transposed_matrix:
        if 0 not in row:
            total_complet_line = sum(row)
            break

if not total_complet_line:
    new_row = [matrix[0][0], matrix[1][1], matrix[2][2]]
    if 0 not in new_row:
        total_complet_line = sum(new_row)
    else:
        new_row = [matrix[0][2], matrix[1][1], matrix[2][0]]
        total_complet_line = sum(new_row)



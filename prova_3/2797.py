"""
IDEIA DE SOLUÇÃO:
"""
rows, columns, min_dist = map(int, input().split())

all_right: bool = True

matrix: list = []
for i in range(rows):
    row: list = list(map(int, input().split()))
    matrix.append(row)

matrix = list(zip(*matrix))
blank_column = True
for row in matrix:
    if row.count(0) != columns:
        if not blank_column:
            all_right = False
            break
        else:
            blank_column = False

    if not blank_column:
        for prove_type in range(1, 3):
            if not all_right:
                break
            current_dist = min_dist
            for studenty in row:
                if studenty != prove_type:
                    current_dist += 1
                else:
                    if current_dist < min_dist:
                        all_right = False
                        break
                    else:
                        current_dist = 0

    if not all_right:
        break

if all_right:
    print('S')
else:
    print('N')

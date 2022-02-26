"""
IDEIA DE SOLUÇÃO: Como no momento de criar a matriz eu já possuo a sua localização, em vez de criar a matriz e depois
verificar quem respeita as regras, optei por já fazer a verificação e assim somar os que respeitam sem necessariamente
ter que criar a matriz.
"""

operation: str = input()
entries_sum: float = 0.0

houses: int = 0
for n_row in range(12):
    for n_column in range(12):
        float_entry: float = float(input())
        second_limit: int = 11 - n_row
        if (n_column < n_row) and (n_column > second_limit):
            houses += 1
            entries_sum += float_entry

if operation == 'S':
    print(round(entries_sum, 1))
elif operation == 'M':
    average = round(entries_sum / houses, 1)
    print(average)

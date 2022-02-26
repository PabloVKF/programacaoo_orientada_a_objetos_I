"""
IDEIA DE SOLUÇÃO: passar por cada tentativa verificando se é a maior até então.
"""

num_houses: int = int(input())
houses: list = list(map(int, input().split()))

best_total: int = 0
for width in range(1, len(houses) + 1):
    for move in range(len(houses)):
        start_range: int = move
        end_range: int = width + move

        if len(houses[start_range:end_range]) < width:
            break

        total: int = sum(houses[start_range:end_range])
        if total > best_total:
            best_total = total

print(best_total)

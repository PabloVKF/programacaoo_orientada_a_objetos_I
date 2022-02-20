pieces_number: int = int(input())
current_pieces: list = list(map(int, input().split()))

# Itera sobre o número de peças informado até que encontre qaul não está na lista de peças.
# Assim que encontrado usa o "break" para poupar processamento, visto que só tera uma peça faltando.
for piece in range(1, pieces_number + 1):
    if piece not in current_pieces:
        print(piece)
        break

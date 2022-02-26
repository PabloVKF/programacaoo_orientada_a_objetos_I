"""
IDEIA DE SOLUÇÃO: Antes de adicionar no array, já validar se esta la ou não e fazer a contagem.
"""

stickers_numbers: int = int(input())
different: int = 0
repeted: int = 0
stickers: list = []
for number in range(stickers_numbers):
    id_sticker: str = input()
    if id_sticker in stickers:
        repeted += 1
    else:
        different += 1
    stickers.append(id_sticker)

print(different)
print(repeted)

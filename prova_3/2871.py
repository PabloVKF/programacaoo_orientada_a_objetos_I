"""
IDEIA DE SOLUÇÃO:Somar direto, sem necessidade de construir a matriz
"""
while True:
    try:
        rows, columns = map(int, input().split())

        total: int = 0
        for i in range(rows):
            total += sum(list(map(int, input().split())))

        sacas = total // 60
        litros = total % 60

        print(f"{sacas} saca(s) e {litros} litro(s)")
    except EOFError:
        break

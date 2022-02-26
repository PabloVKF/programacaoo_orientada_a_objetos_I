"""
IDEIA DE SOLUÇÃO: Fiz regra de 3 com n/x = m/y para saber o valor minimo que y deve apresentar
para estar acima do rio (limit)
"""

n, m, soldiers = map(int, input().split())
army_1: int = 0
army_2: int = 0
for number in range(soldiers):
    x, y, force = map(int, input().split())
    min_y = (x * m) / n
    if y > min_y:
        army_1 += force
    else:
        army_2 += force

print(army_1, army_2)

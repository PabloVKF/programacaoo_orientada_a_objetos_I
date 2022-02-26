"""
IDEIA DE SOLUÇÃO:
"""

import numpy as np
from numpy import linalg

matrix: list = []
for number in range(4):
    point: list = list(map(int, input().split()))
    matrix.append(point)
quadrilateral_1 = np.array(matrix)
area_1: int = np.linalg.det(quadrilateral_1)

matrix: list = []
for number in range(4):
    point: list = list(map(int, input().split()))
    matrix.append(point)
quadrilateral_2 = np.array(matrix)
area_2: int = np.linalg.det(quadrilateral_2)

if area_1 > area_2:
    print("terreno A")
else:
    print("terreno B")

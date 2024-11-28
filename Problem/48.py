import math
from typing import List

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    L = []
    n = len(matrix)
    for x in range(n):
        ln = []
        for y in range(n):
            ln.append(matrix[y][x])
        L.append(ln)

    for row in range(n):
        L[row].reverse()
        matrix[row] = L[row]

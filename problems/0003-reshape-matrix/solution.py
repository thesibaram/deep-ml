import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    if not a or not a[0]:
        return []
    m, n = new_shape
    if m *n != len(a[0])*len(a):
        return []

    flat= [item for row in a for item in row]
    return [flat[i*n: (i+1)*n]for i in range(m)]
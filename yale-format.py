"""Sparse matrix multiplication with Yale format compression

https://leetcode.com/problems/sparse-matrix-multiplication/
"""

from typing import NamedTuple


class YaleFormat(NamedTuple):
    values: list[int]
    row_indices: list[int]
    col_indices: list[int]


def compress(mat: list[list[int]], col_wise: bool) -> YaleFormat:
    return compress_col_wise(mat) if col_wise else compress_row_wise(mat)


def compress_row_wise(mat: list[list[int]]) -> YaleFormat:
    m, n = len(mat), len(mat[0])
    values = []
    row_indices = [0] * (m + 1)
    col_indices = []

    for r in range(m):
        for c in range(n):
            if val := mat[r][c]:
                values.append(val)
                col_indices.append(c)
        row_indices[r + 1] = len(values)

    return YaleFormat(values, row_indices, col_indices)


def compress_col_wise(mat: list[list[int]]) -> YaleFormat:
    m, n = len(mat), len(mat[0])
    values = []
    row_indices = []
    col_indices = [0] * (n + 1)

    for c in range(n):
        for r in range(m):
            if val := mat[r][c]:
                values.append(val)
                row_indices.append(r)
        col_indices[c + 1] = len(values)

    return YaleFormat(values, row_indices, col_indices)


def multiply(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    # mat1: m x k, mat2: k x n
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    a, b = compress(mat1, col_wise=False), compress(mat2, col_wise=True)

    ans = [[0] * n for _ in range(m)]

    for row in range(m):
        for col in range(n):
            a_start, a_end = a.row_indices[row], a.row_indices[row + 1]
            b_start, b_end = b.col_indices[col], b.col_indices[col + 1]

            while a_start < a_end and b_start < b_end:
                if a.col_indices[a_start] == b.row_indices[b_start]:
                    ans[row][col] += a.values[a_start] * b.values[b_start]
                    a_start += 1
                    b_start += 1
                elif a.col_indices[a_start] < b.row_indices[b_start]:
                    a_start += 1
                else:
                    b_start += 1

    return ans


if __name__ == "__main__":
    mat1 = [
        [1, 0, 0],
        [-1, 0, 3],
    ]
    mat2 = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    expected = [
        [7, 0, 0],
        [-7, 0, 3],
    ]
    
    print("CSR:", compress(mat1, col_wise=False))
    print("CSC:", compress(mat2, col_wise=True))
    
    assert multiply(mat1, mat2) == expected

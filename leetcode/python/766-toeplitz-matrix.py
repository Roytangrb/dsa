# Author: RT
# Date: 2022-10-31T14:09:31.756Z
# URL: https://leetcode.com/problems/toeplitz-matrix/


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        # x x x x
        # o x x x
        # o o x x
        # first loop check 'x' diags, second loop check 'o' diags
        return all(
            len(set(matrix[i][c + i] for i in range(min(m, n - c)))) == 1
            for c in range(n)
        ) and all(
            len(set(matrix[r + i][i] for i in range(min(m - r, n)))) == 1
            for r in range(1, m)
        )

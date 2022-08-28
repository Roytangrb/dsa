# Author: RT
# Date: 2022-08-28T09:04:48.110Z
# URL: https://leetcode.com/problems/sort-the-matrix-diagonally/


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        for col in range(n):
            length = min(n - col, m)
            arr = sorted([mat[i][col + i] for i in range(length)])
            for i, num in enumerate(arr):
                mat[i][col + i] = num

        for row in range(1, m):
            length = min(m - row, n)
            arr = [mat[row + i][i] for i in range(length)]
            for i, num in enumerate(sorted(arr)):
                mat[row + i][i] = num

        return mat

# Author: RT
# Date: 2022-12-13T14:25:38.175Z
# URL: https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for r in range(1, m):
            prev = matrix[r - 1]
            for c in range(n):
                v = matrix[r][c]
                matrix[r][c] = v + prev[c]
                if c - 1 > -1:
                    matrix[r][c] = min(matrix[r][c], prev[c - 1] + v)
                if c + 1 < n:
                    matrix[r][c] = min(matrix[r][c], prev[c + 1] + v)

        return min(matrix[-1])

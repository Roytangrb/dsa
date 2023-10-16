# Author: RT
# Date: 2023-10-16T21:31:01.408Z
# URL: https://leetcode.com/problems/pascals-triangle-ii/description/


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """Value of (r, c) in Pascal's Triangle = combination(r, c)"""
        n = rowIndex + 1
        ans = [1] * n
        v, d_denominator, d_numerator = 1, 1, rowIndex
        for j in range(1, n):
            v = v * d_numerator // d_denominator
            ans[j] = v
            d_denominator += 1
            d_numerator -= 1

        return ans

    def getRow__brute_force(self, rowIndex: int) -> list[int]:
        """O(n)"""
        n = rowIndex + 1
        mat = [[1] * n for _ in range(n)]
        for r in range(1, n):
            for c in range(1, r):
                mat[r][c] = mat[r - 1][c - 1] + mat[r - 1][c]

        return mat[-1]

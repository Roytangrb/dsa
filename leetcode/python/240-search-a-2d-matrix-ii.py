# Author: RT
# Date: 2022-07-24T10:21:34.183Z
# URL: https://leetcode.com/problems/search-a-2d-matrix-ii/


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            curr = matrix[i][j]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return True

        return False

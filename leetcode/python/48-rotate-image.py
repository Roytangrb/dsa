# Author: RT
# Date: 2022-08-30T13:37:14.609Z
# URL: https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left = 0
        right = n - 1

        while left < right:
            top = left
            bottom = right
            for i in range(right - left):
                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            left += 1
            right -= 1

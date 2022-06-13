# Author: RT
# Date: 2022-06-13T15:10:48.979Z
# URL: https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        h = len(triangle)
        for i in range(1, h):
            for j in range(i + 1):
                top_left = (
                    float("inf") if j == 0 else triangle[i - 1][j - 1] + triangle[i][j]
                )
                top_right = (
                    float("inf") if j == i else triangle[i - 1][j] + triangle[i][j]
                )
                triangle[i][j] = min(top_left, top_right)

        return min(triangle[-1])

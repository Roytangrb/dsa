# Author: RT
# Date: 2023-06-08T04:10:19.659Z
# URL: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = 0, n - 1
        ans = 0
        while r < m and c >= 0:
            curr = grid[r][c]
            if curr < 0:
                if c > 0:
                    c -= 1
                else:
                    ans += n * (m - r)
                    break
            else:
                ans += n - 1 - c
                r += 1

        return ans

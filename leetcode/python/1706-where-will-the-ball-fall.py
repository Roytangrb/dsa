# Author: RT
# Date: 2022-11-01T13:56:39.545Z
# URL: https://leetcode.com/problems/where-will-the-ball-fall/


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for ball in range(n):
            r = 0
            c = ball
            while r < m:
                left = grid[r][c] == -1
                right = not left
                can_left = c > 0 and grid[r][c - 1] == -1
                can_right = c < n - 1 and grid[r][c + 1] == 1
                if left and can_left:
                    r += 1
                    c -= 1
                elif right and can_right:
                    r += 1
                    c += 1
                else:
                    break

            ans.append(c if r == m else -1)

        return ans

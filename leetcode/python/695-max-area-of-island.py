# Author: RT
# Date: 2022-07-15T07:26:41.327Z
# URL: https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if not grid[i][j]:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans

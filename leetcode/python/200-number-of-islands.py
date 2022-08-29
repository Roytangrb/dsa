# Author: RT
# Date: 2022-08-29T13:10:36.050Z
# URL: https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i in range(m) and j in range(n) and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans

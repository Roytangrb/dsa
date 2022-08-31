# Author: RT
# Date: 2022-08-31T10:38:15.609Z
# URL: https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        alantic = [[False] * n for _ in range(m)]

        def flow_up_dfs(i, j, prev, grid):
            if (
                i in range(m)
                and j in range(n)
                and not grid[i][j]
                and heights[i][j] >= prev
            ):
                grid[i][j] = True
                h = heights[i][j]
                flow_up_dfs(i - 1, j, h, grid)
                flow_up_dfs(i + 1, j, h, grid)
                flow_up_dfs(i, j - 1, h, grid)
                flow_up_dfs(i, j + 1, h, grid)

        for i in range(n):
            flow_up_dfs(0, i, 0, pacific)
            flow_up_dfs(m - 1, i, 0, alantic)
        for i in range(m):
            flow_up_dfs(i, 0, 0, pacific)
            flow_up_dfs(i, n - 1, 0, alantic)

        return [
            [i, j]
            for i in range(m)
            for j in range(n)
            if pacific[i][j] and alantic[i][j]
        ]

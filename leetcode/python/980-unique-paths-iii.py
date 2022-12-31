# Author: RT
# Date: 2022-12-31T04:26:21.027Z
# URL: https://leetcode.com/problems/unique-paths-iii/


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        S, T, E, W = 1, 2, 0, -1

        def backtrack(i: int, j: int, remain: int):
            if 0 <= i < m and 0 <= j < n and grid[i][j] < 3:
                if grid[i][j] is T and remain == 1:
                    return 1
                if grid[i][j] in (S, E):
                    grid[i][j] += 4
                    ret = (
                        backtrack(i + 1, j, remain - 1)
                        + backtrack(i - 1, j, remain - 1)
                        + backtrack(i, j + 1, remain - 1)
                        + backtrack(i, j - 1, remain - 1)
                    )
                    grid[i][j] -= 4
                    return ret

            return 0

        si, sj = 0, 0
        vc = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] is S:
                    si, sj = i, j
                if grid[i][j] is not W:
                    vc += 1

        return backtrack(si, sj, vc)

# Author: RT
# Date: 2022-07-16T14:31:16.073Z
# URL: https://leetcode.com/problems/out-of-boundary-paths/


from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        M = 10**9 + 7
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @cache
        def dfs(i: int, j: int, count: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if not count:
                return 0
            return sum(dfs(i + dx, j + dy, count - 1) for dx, dy in dirs) % M

        return dfs(startRow, startColumn, maxMove) % M

    def find_paths__dp_bottom_up(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        M = 10**9 + 7
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        # represent count of ways to reach cell (i, j) given x moves
        # iterate for move in 0..maxMove, if a cell's count > 0, accumulate to
        # adjacent cells, if adjacent cell(s) is out of bound, add to answer
        ans = 0
        dp = [[0] * n for _ in range(m)]
        # initial state: move = 0
        dp[startRow][startColumn] = 1
        for move in range(1, maxMove + 1):
            # all balls within a move happen at the same time
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if not dp[i][j]:
                        continue
                    outbounds = (i == 0) + (i == m - 1) + (j == 0) + (j == n - 1)
                    ans = (ans + dp[i][j] * outbounds) % M
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n:
                            temp[x][y] += dp[i][j] % M
            dp = temp

        return ans

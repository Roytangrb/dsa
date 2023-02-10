# Author: RT
# Date: 2023-02-10T14:41:29.222Z
# URL: https://leetcode.com/problems/as-far-from-land-as-possible/


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        q = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 1]
        if len(q) in (0, n * n):
            return -1

        ans = 0
        # multi-source bfs
        while q:
            frontier = []
            for r, c in q:
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        frontier.append((nr, nc))

            q = frontier
            ans += 1

        return ans - 1  # last frontier has only one 1-node

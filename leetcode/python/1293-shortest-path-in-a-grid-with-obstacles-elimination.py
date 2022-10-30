# Author: RT
# Date: 2022-10-30T15:58:57.487Z
# URL: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/


from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        return self.shortestPath__bfs(grid, k)

    def shortestPath__a_star(self, grid: list[list[int]], k: int) -> int:
        pass  # TODO:

    def shortestPath__bfs(self, grid: list[list[int]], k: int) -> int:
        """BFS + keep track of k state in visited"""
        m, n = len(grid), len(grid[0])
        seen = set()
        q = deque([(0, 0, 0, 0)])
        while q:
            r, c, x, steps = q.popleft()
            if grid[r][c]:
                x += 1
            if x > k:
                continue
            if (r, c) == (m - 1, n - 1):
                return steps
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n and (nr, nc, x) not in seen:
                    seen.add((nr, nc, x))
                    q.append((nr, nc, x, steps + 1))

        return -1

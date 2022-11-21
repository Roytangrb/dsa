# Author: RT
# Date: 2022-11-21T14:15:25.612Z
# URL: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/


from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        is_exit = lambda x: x[0] in (0, m - 1) or x[1] in (0, n - 1)

        q: deque[tuple[int, int, int]] = deque([(*entrance, 0)])
        maze[entrance[0]][entrance[1]] = "x"
        while q:
            i, j, dist = q.popleft()
            if is_exit((i, j)) and [i, j] != entrance:
                return dist

            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                    maze[x][y] = "x"
                    q.append((x, y, dist + 1))

        return -1

# Author: RT
# Date: 2022-05-24T16:32:50.704Z
# URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        radj, outdegree = defaultdict(list), {}
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x in range(m):
            for y in range(n):
                outdegree[(x, y)] = 0
                for dx, dy in dirs:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < m and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
                        outdegree[(x, y)] += 1
                        radj[(nx, ny)].append((x, y))
        q = [v for v, d in outdegree.items() if not d]

        ans = 0
        while q:
            frontier = []
            ans += 1
            for v in q:
                for u in radj[v]:
                    outdegree[u] -= 1
                    if not outdegree[u]:
                        frontier.append(u)
            q = frontier

        return ans

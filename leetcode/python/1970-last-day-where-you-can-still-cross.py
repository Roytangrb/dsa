# Author: RT
# Date: 2023-06-30T03:54:19.274Z
# URL: https://leetcode.com/problems/last-day-where-you-can-still-cross/description/


from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        G = [[0] * col for _ in range(row)]
        for day, cell in enumerate(cells):
            r, c = cell
            G[r - 1][c - 1] = day + 1

        left, right = 1, len(cells) - row + 1
        # bisect_right
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.can_cross(row, col, G, mid):
                left = mid
            else:
                right = mid - 1

        return left

    def can_cross(self, row: int, col: int, G: list[list[int]], start_day: int) -> bool:
        # As long as there 1 ok path on given start day, return true
        q = deque(
            [(0, start_col) for start_col in range(col) if start_day < G[0][start_col]]
        )

        visited = set()
        while q:
            r, c = q.popleft()
            if r == row - 1:
                return True

            visited.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < row
                    and 0 <= nc < col
                    and start_day < G[nr][nc]
                    and (nr, nc) not in visited
                ):
                    q.append((nr, nc))

        return False

# Author: RT
# Date: 2023-05-21T06:36:40.067Z
# URL: https://leetcode.com/problems/shortest-bridge/


class Solution:
    external_cells: list[tuple[int, int]]

    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        self.external_cells = []
        ir, ic = next((r, c) for r in range(n) for c in range(n) if grid[r][c] == 1)
        self.dfs(grid, n, ir, ic, 2)

        # Use first found island as start, BFS found shortest path length to another island
        q = self.external_cells
        ans = 0  # Start cell not part of the bridge
        while q:
            frontier = []
            for r, c in q:
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            frontier.append((nr, nc))
                        elif grid[nr][nc] != 2:
                            return ans  # End cell not part of the bridge

            q = frontier
            ans += 1

        return -1

    def dfs(self, grid, n, r, c, v) -> bool:
        """Change label of island, memorize internal cells.
        Returns whether current node is in island or is map boundary."""
        if 0 <= r < n and 0 <= c < n:
            if grid[r][c] == 1:
                grid[r][c] = v
                is_internal = True
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    # dfs needs to be called, do not short circuit
                    is_internal = self.dfs(grid, n, r + dr, c + dc, v) and is_internal
                if not is_internal:
                    self.external_cells.append((r, c))

                return True
            else:
                return False

        return True

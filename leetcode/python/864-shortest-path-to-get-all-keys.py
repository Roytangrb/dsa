# Author: RT
# Date: 2023-06-29T00:06:00.611Z
# URL: https://leetcode.com/problems/shortest-path-to-get-all-keys/description/


from collections import defaultdict, deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n, KEYS = len(grid), len(grid[0]), frozenset("abcdef")
        # init
        keys = set()
        all_keys = 0
        sr = sc = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell in KEYS:
                    keys.add(cell)
                    all_keys = self.store_key(all_keys, cell)
                elif cell == "@":
                    sr, sc = r, c

        # BFS
        seen_by_keys_state = defaultdict(set)
        q = deque([(sr, sc, 0, 0)])
        while q:
            r, c, keys_state, dist = q.popleft()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (cell := grid[nr][nc]) != "#"
                    and (nr, nc) not in seen_by_keys_state[keys_state]
                ):
                    if cell in keys:
                        # new state visiting current direction
                        new_state = self.store_key(keys_state, cell)
                        if new_state == all_keys:
                            return dist + 1

                        seen_by_keys_state[new_state].add((nr, nc))
                        q.append((nr, nc, new_state, dist + 1))
                    elif cell.lower() in keys and not self.has_key(
                        keys_state, cell.lower()
                    ):
                        continue
                    else:  # has key to go over lock or empty cell
                        seen_by_keys_state[keys_state].add((nr, nc))
                        q.append((nr, nc, keys_state, dist + 1))

        return -1

    def get_key_id(self, key: str) -> int:
        return 1 << ord(key) - ord("a")

    def has_key(self, keys_state: int, key: str) -> bool:
        return bool(keys_state & self.get_key_id(key))

    def store_key(self, keys_state: int, key: str) -> int:
        return keys_state | self.get_key_id(key)

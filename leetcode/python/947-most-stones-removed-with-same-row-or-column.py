# Author: RT
# Date: 2022-11-14T14:32:27.099Z
# URL: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """Union-by-rank, count components, all stones in a component can be
        removed except for the last one"""
        # NOTE: union-by-size and sum and sizes does not work because some nodes
        # are counted multiple times while merging two components during union.
        n = len(stones)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            rx, ry = rank[x], rank[y]
            if rx > ry:
                parent[py] = px
                return px
            elif rx < ry:
                parent[px] = py
                return py
            else:
                parent[px] = py
                rank[py] += 1
                return py

        rows = {}
        cols = {}
        for i, stone in enumerate(stones):
            r, c = stone
            if r in rows:
                union(rows[r], i)
            rows[r] = i
            if c in cols:
                union(cols[c], i)
            cols[c] = i

        components = sum(1 for i in range(n) if find(i) == i)
        return n - components

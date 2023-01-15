# Author: RT
# Date: 2023-01-15T02:40:40.526Z
# URL: https://leetcode.com/problems/number-of-good-paths/

from collections import Counter, defaultdict
from itertools import groupby


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        parents = list(range(n))
        ranks = [0] * n

        ans = 0
        vfn = lambda x: x[1]
        vals_nodes_map = {
            v: list(nodes)
            for v, nodes in groupby(sorted(enumerate(vals), key=vfn), key=vfn)
        }
        for val in sorted(vals_nodes_map.keys()):
            # for current val (larger than all values processed so far)
            # there are (n + 1) * n // 2 paths within the same connected component,
            # n = number of nodes in the component.
            for x, _ in vals_nodes_map[val]:
                for neighbor in adj[x]:
                    if vals[neighbor] <= val:
                        self.union(neighbor, x, parents, ranks)

            ans += sum(
                (size + 1) * size // 2
                for size in Counter(
                    self.find(x, parents) for x, _ in vals_nodes_map[val]
                ).values()
            )

        return ans

    def find(self, x: int, parents: list[int]) -> int:
        if parents[x] != x:
            parents[x] = self.find(parents[x], parents)

        return parents[x]

    def union(self, x: int, y: int, parents: list[int], ranks: list[int]):
        px, py = self.find(x, parents), self.find(y, parents)
        if px == py:
            return

        rx, ry = ranks[x], ranks[y]
        if rx < ry:
            px, py = py, px

        parents[py] = px
        if rx == ry:
            ranks[px] += 1

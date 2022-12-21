# Author: RT
# Date: 2022-12-21T14:12:11.194Z
# URL: https://leetcode.com/problems/possible-bipartition/


from collections import defaultdict
from typing import Literal, Optional


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        G = defaultdict(list)
        for u, v in dislikes:
            G[u].append(v)
            G[v].append(u)

        colors: list[Optional[int]] = [None] * (n + 1)

        def dfs(u: int, prev: Literal[0, 1]) -> bool:
            """Return whether two-coloring (0|1) of the graph is possible"""
            if colors[u] is not None:
                return colors[u] != prev

            curr = prev ^ 1
            colors[u] = curr

            return all(dfs(v, curr) for v in G[u])

        # bipartite graph can be disconnected
        # each dfs call will color the connected subgraph
        # start dfs if only the vertex is not colored yet
        return all(dfs(u, 0) for u in range(1, n + 1) if colors[u] is None)

"""Test if a graph is bipartite

https://leetcode.com/problems/is-graph-bipartite/
A bipartite graph is a graph without odd length cycles. Use two-coloring to detect
odd length cycles (dfs try assign vertex with color different from parent's).
"""

from typing import Optional


def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    colors: list[Optional[int]] = [None] * n

    def dfs(u: int, prev: int):
        """Return whether two-coloring (0|1) of the graph is possible"""
        if colors[u] is not None:
            return colors[u] != prev

        curr = prev ^ 1
        colors[u] = curr

        return all(dfs(v, curr) for v in graph[u])

    # bipartite graph can be disconnected
    # each dfs call will color the connected subgraph
    # start dfs if only the vertex is not colored yet
    return all(dfs(u, 0) for u in range(n) if colors[u] is None)


if __name__ == "__main__":
    testcases = (
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    )

    for adj, expected in testcases:
        assert is_bipartite(adj) == expected

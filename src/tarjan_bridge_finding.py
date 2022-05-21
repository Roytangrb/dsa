"""Tarjan's off-line bridge finding algorithm

https://leetcode.com/problems/critical-connections-in-a-network/

Definition of bridge:
    Deletion of a bridge increases the graph's number of connected components

Ref: https://cp-algorithms.com/graph/bridge-searching.html#algorithm
"""

from collections import defaultdict


def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    bridges = []
    visited = [False] * n
    entry_time = [-1] * n
    min_time = [float("inf")] * n
    timer = 0

    def dfs(u, parent):
        nonlocal timer

        visited[u] = True
        timer += 1
        entry_time[u] = min_time[u] = timer

        for v in adj[u]:
            # edge to parent does not count as back-edge to parent's ancestor
            if v == parent:
                continue

            if visited[v]:
                # vertex u has an back-edge to parent's ancestor
                # update min_time of u to earliest ancestor's entry time
                min_time[u] = min(min_time[u], entry_time[v])
            else:
                dfs(v, u)
                # sub-tree of vertex u (vertcies visited later in dfs) has
                # back-edge(s) to ancestor(s) of u if min_time[v] < entry_time[u],
                # otherwise, (u, v) is a bridge
                if min_time[v] > entry_time[u]:
                    bridges.append([u, v])

                # update min_time of u to sub-tree's min_time
                min_time[u] = min(min_time[u], min_time[v])

    # in this question, graph is connected, start dfs once
    # in disconnected graph, start dfs if vertex not visited to find in all components
    dfs(connections[0][0], -1)
    return bridges


if __name__ == "main":
    testcases = (
        (4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]),
        (2, [[0, 1]], [[0, 1]]),
    )

    for n, edges, expected in testcases:
        assert critical_connections(n, edges) == expected

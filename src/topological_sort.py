"""Topological Sort"""

from collections import defaultdict, deque


def is_graph_valid_tree(n: int, edges: list[list[int]]) -> bool:
    """Determine a undirectred graph with n nodes is a valid tree

    https://leetcode.com/problems/graph-valid-tree/
    """
    # graph with only single node and no edges
    if n == 1:
        return True

    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # start topological sort with leave nodes (indegree=1)
    q = deque([])
    for u in adj:
        # disconnected node
        if not (indegree := len(adj[u])):
            return False
        elif indegree == 1:
            q.append(u)

    visited_count = 0
    root_count = 0
    while q:
        u = q.popleft()
        visited_count += 1

        if not adj[u]:
            root_count += 1

        for v in adj[u]:
            adj[v].remove(u)
            if len(adj[v]) == 1:
                q.append(v)

    # graph is a tree if there is no cycle and there's only one component
    return visited_count == n and root_count == 1


def test_is_graph_valid_tree():
    testcases = (
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),  # valid
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),  # cycle
        (4, [[0, 1], [2, 3]], False),  # two components
        (1, [], True),  # single node
    )

    for n, edges, expected in testcases:
        assert is_graph_valid_tree(n, edges) == expected


if __name__ == "__main__":
    test_is_graph_valid_tree()

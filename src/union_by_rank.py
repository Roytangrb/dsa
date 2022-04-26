"""Disjoint Set Union Find, union by component rank"""


def is_graph_valid_tree(n: int, edges: list[list[int]]) -> bool:
    """Determine a undirectred graph with n nodes is a valid tree

    https://leetcode.com/problems/graph-valid-tree/
    """
    parent = [i for i in range(n)]
    rank = [0] * n

    for x, y in edges:
        # if x and y are already merged, adding the edge introduce cycle
        if not union(x, y, parent, rank):
            return False

    root_count = sum(1 for i in range(n) if find(i, parent) == i)

    return root_count == 1


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank) -> bool:
    """Returns True if union happened (x and y are not in the same component)"""
    px = find(x, parent)
    py = find(y, parent)
    if px == py:
        return False

    rx = rank[px]
    ry = rank[py]
    if rx > ry:
        parent[py] = px
    elif ry > rx:
        parent[px] = py
    else:
        parent[py] = px
        rank[px] += 1

    return True


if __name__ == "main":
    testcases = (
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),  # valid
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),  # cycle
        (4, [[0, 1], [2, 3]], False),  # two components
        (1, [], True),  # single node
    )

    for n, edges, expected in testcases:
        assert is_graph_valid_tree(n, edges) == expected

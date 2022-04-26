"""Kruskal's algorithm for finding minimum spanning tree

https://leetcode.com/problems/min-cost-to-connect-all-points/
"""

import union_by_rank


def minimum_spanning_tree(points: list[list[int]]) -> int:
    n = len(points)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            # cost of edge represented by Manhattan distance
            edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))

    # use lowest-weighted edge, if the vertices are not connected
    # (thus no cycle will be formed), then add the edge to the MST
    parent = [i for i in range(n)]
    rank = [0] * n
    ans = 0
    for cost, u, v in sorted(edges):
        if union_by_rank.union(u, v, parent, rank):
            ans += cost

    return ans


if __name__ == "main":
    testcases = (
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    )

    for points, expected in testcases:
        assert minimum_spanning_tree(points) == expected

"""Prim's algorithm for finding minimum spanning tree, using priority queue

https://leetcode.com/problems/min-cost-to-connect-all-points/
"""

import heapq


def minimum_spanning_tree(points: list[list[int]]) -> int:
    """O(|E|log(|V|)) implementation with binary heap"""
    n = len(points)
    seen = [False] * n
    edge_count = 0
    # start at arbitrary vertex (0)
    # using a dummy edge with weight 0 to vertex 0 itself
    pq = [(0, 0)]

    ans = 0
    # MST has n - 1 edges, the loop counts 1 more iteration for the dummy edge
    while edge_count < n:
        weight, u = heapq.heappop(pq)

        # if current vertex is seen, discard edge to the current vertex
        if seen[u]:
            continue

        seen[u] = True
        ans += weight
        edge_count += 1

        # add edges to unseen vertices reachable from the current vertex
        # to the min heap
        for v in range(n):
            if not seen[v]:
                next_weight = abs(points[u][0] - points[v][0]) + abs(
                    points[u][1] - points[v][1]
                )
                heapq.heappush(pq, (next_weight, v))

    return ans


if __name__ == "main":
    testcases = (
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    )

    for points, expected in testcases:
        assert minimum_spanning_tree(points) == expected

"""Dijkstra algorithm, single source shortest-path algorithm for directed graph
with non-negative edge weights.

https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
"""

import heapq
from collections import defaultdict


def dijkstra(graph: dict[int, list], source: int, n: int):
    """Using min binary heap and lazy deletion"""
    pq, dist = [(0, source)], {}
    while pq:
        cost, curr = heapq.heappop(pq)
        if curr not in dist:
            dist[curr] = cost
            for neighbor, weight in graph[curr]:
                heapq.heappush(pq, (cost + weight, neighbor))

    return [dist.get(i, float("inf")) for i in range(n)]


def minimum_weight_subgraph(
    n: int, edges: list[list[int]], src1: int, src2: int, dest: int
) -> int:
    adj = defaultdict(list)
    radj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        radj[v].append((u, w))

    # src1's and src2's paths to dest has common vertex x (including dest itself)
    # find x such that sum of distances src1->x, src2->x, and dest->x (using the
    # reversed graph) is minimal.
    src1_x = dijkstra(adj, src1, n)
    src2_x = dijkstra(adj, src2, n)
    dest_x = dijkstra(radj, dest, n)

    ans = min(src1_x[x] + src2_x[x] + dest_x[x] for x in range(n))

    # if distance is inf, there's no such subgraph
    return ans if ans != float("inf") else -1


if __name__ == "main":
    assert (
        minimum_weight_subgraph(
            n=6,
            edges=[
                [0, 2, 2],
                [0, 5, 6],
                [1, 0, 3],
                [1, 4, 5],
                [2, 1, 1],
                [2, 3, 3],
                [2, 3, 4],
                [3, 4, 2],
                [4, 5, 1],
            ],
            src1=0,
            src2=1,
            dest=5,
        )
        == 9
    )

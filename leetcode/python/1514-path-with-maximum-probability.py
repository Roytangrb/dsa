# Author: RT
# Date: 2023-06-28T03:37:08.692Z
# URL: https://leetcode.com/problems/path-with-maximum-probability/description/


import heapq
from collections import defaultdict


def dijkstra(graph: dict[int, list], source: int, n: int):
    # use negative of prob as distance
    pq, dist = [(-1, source)], {}
    while pq:
        t, curr = heapq.heappop(pq)
        if curr not in dist:
            dist[curr] = -t
            for neighbor, w in graph[curr]:
                heapq.heappush(pq, (t * w, neighbor))

    return [dist.get(i, 0) for i in range(n)]


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int,
    ) -> float:
        G = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            u, v = edge
            G[u].append((v, prob))
            G[v].append((u, prob))

        dist = dijkstra(G, start, n)
        return dist[end]

# Author: RT
# Date: 2023-01-26T05:21:17.250Z
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/


import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        G = defaultdict(list)
        for u, v, w in flights:
            G[u].append((v, w))

        # priority queue (cost, node, edges)
        pq, stops = [(0, src, 0)], defaultdict(lambda: float("inf"))
        while pq:
            cost, curr, edges = heapq.heappop(pq)
            if curr == dst:
                return cost

            # if there exists a shortest path within k stops, dijkstra algo
            # will have returned the min cost, otherwise,
            # replace path to seen node if it takes fewer stops.
            if edges < stops[curr] and edges <= k:
                stops[curr] = edges
                for neighbor, weight in G[curr]:
                    heapq.heappush(pq, (cost + weight, neighbor, edges + 1))

        return -1

# Author: RT
# Date: 2023-02-12T07:10:14.351Z
# URL: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/


import math
from collections import defaultdict


class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        G = defaultdict(list)
        for u, v in roads:
            G[u].append(v)
            G[v].append(u)

        ans = 0

        def dfs(node: int, parent: int) -> int:
            nonlocal ans

            passengers = (
                sum(
                    dfs(child, node)
                    for child in G[node]
                    if child != parent  # prevent re-visiting
                )
                + 1
            )

            # fuel needed for all passengers in the current
            # subtree to reach the parent node
            if node != 0:
                ans += math.ceil(passengers / seats)

            return passengers

        dfs(0, 0)

        return ans

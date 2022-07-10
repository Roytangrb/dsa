# Author: RT
# Date: 2022-07-10T14:01:37.839Z
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        p1 = p2 = 0

        for i in range(2, n + 1):
            p1, p2 = min(p1 + cost[i - 1], p2 + cost[i - 2]), p1

        return p1

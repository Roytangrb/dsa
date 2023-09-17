# Author: RT
# Date: 2023-09-17T04:08:01.134Z
# URL: https://leetcode.com/problems/maximum-number-of-alloys/description/


import math


class Solution:
    def maxNumberOfAlloys(
        self,
        n,
        k,
        budget,
        composition: list[list[int]],
        stock: list[int],
        cost: list[int],
    ) -> int:
        return max(self.solve(n, budget, comp, stock, cost) for comp in composition)

    def solve(self, n, budget, comp, stock, cost):
        unit_cost = sum(comp[i] * cost[i] for i in range(n))

        l, r = (
            0,
            max(math.ceil(stock[i] / comp[i]) for i in range(n))
            + math.ceil(budget / unit_cost)
            + 1,
        )
        while l < r:
            created = l + (r - l + 1) // 2
            used = 0
            for i in range(n):
                needs = max(comp[i] * created - stock[i], 0)
                used += needs * cost[i]
            if used <= budget:
                l = created
            else:
                r = created - 1

        return l

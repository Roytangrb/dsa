# Author: RT
# Date: 2022-07-14T15:56:26.215Z
# URL: https://leetcode.com/problems/paint-house-iii/

from functools import cache


class Solution:
    def minCost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:
        @cache
        def dp(house: int, prev_color: int, nbcount: int):
            if house == m:
                return 0 if nbcount == target else float("inf")
            if nbcount > target:
                return float("inf")

            min_cost = float("inf")
            if painted := houses[house]:
                min_cost = min(
                    min_cost, dp(house + 1, painted, nbcount + (painted != prev_color))
                )
            else:
                for color in range(1, n + 1):
                    min_cost = min(
                        min_cost,
                        dp(house + 1, color, nbcount + (color != prev_color))
                        + cost[house][color - 1],
                    )
            return min_cost

        ans = dp(0, None, 0)
        return ans if ans != float("inf") else -1

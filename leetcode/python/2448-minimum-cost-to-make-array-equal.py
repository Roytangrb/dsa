# Author: RT
# Date: 2023-06-21T03:57:05.075Z
# URL: https://leetcode.com/problems/minimum-cost-to-make-array-equal/


from itertools import accumulate


class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        nums_costs = sorted(zip(nums, cost))
        n = len(nums_costs)
        prefix_cost_sum = list(accumulate((cost for _, cost in nums_costs)))
        # when target = smallest num
        total_cost = sum((num - nums_costs[0][0]) * cost for num, cost in nums_costs)
        ans = total_cost
        for i in range(1, n):
            gap = nums_costs[i][0] - nums_costs[i - 1][0]
            total_cost += (
                prefix_cost_sum[i - 1] * gap
                - (prefix_cost_sum[n - 1] - prefix_cost_sum[i - 1]) * gap
            )
            ans = min(ans, total_cost)

        return ans

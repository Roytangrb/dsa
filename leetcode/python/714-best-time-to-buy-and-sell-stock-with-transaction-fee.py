# Author: RT
# Date: 2023-06-22T02:49:41.485Z
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]

    def maxProfit__space_optimized(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0
        for i in range(1, n):
            prev_hold, prev_free = hold, free
            hold = max(prev_hold, prev_free - prices[i])
            free = max(prev_free, prev_hold + prices[i] - fee)

        return free

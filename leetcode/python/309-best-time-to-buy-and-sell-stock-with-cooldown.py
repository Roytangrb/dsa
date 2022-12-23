# Author: RT
# Date: 2022-12-23T09:59:04.474Z
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        # rest[i] = max(rest[i-1], sell[i-1])
        # hold[i] = max(rest[i-1] - prices[i], hold[i-1])
        # sell[i] = hold[i-1] + prices[i]

        prev_rest = 0
        prev_hold = -prices[0]
        prev_sell = 0
        for i in range(1, n):
            price = prices[i]
            curr_rest = max(prev_rest, prev_sell)
            curr_hold = max(prev_rest - price, prev_hold)
            curr_sell = prev_hold + price
            prev_rest, prev_hold, prev_sell = curr_rest, curr_hold, curr_sell

        return max(prev_rest, prev_sell)

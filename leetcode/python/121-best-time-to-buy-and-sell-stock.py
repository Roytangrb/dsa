# Author: RT
# Date: 2023-02-25T05:44:26.042Z
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        buy = float("inf")

        for price in prices:
            if price > buy:
                ans = max(ans, price - buy)
            else:
                buy = price

        return ans

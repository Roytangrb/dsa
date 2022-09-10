# Author: RT
# Date: 2022-09-10T08:24:01.869Z
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)

        if not prices or not k:
            return 0

        # k is large enough and does not limit number of transactions
        if 2 * k > n:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        # dp[i][used_k][holding] = profit
        # holding: 0 not holding, 1 holding
        dp = [[[-1001] * 2 for _ in range(k + 1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, n):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # holding state is not possible when j=0
                if j:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return max(dp[n - 1][j][0] for j in range(k + 1))

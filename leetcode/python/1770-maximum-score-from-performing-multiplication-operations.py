# Author: RT
# Date: 2022-09-16T14:27:43.364Z
# URL: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n, m = len(nums), len(multipliers)

        # dp[i][j] max score after applied i multiply
        # and used j from the left
        dp = [[float("-inf")] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            mul = multipliers[i - 1]
            for j in range(i + 1):
                if j:
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i - 1][j - 1] + mul * nums[j - 1],
                    )
                if j != i:
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i - 1][j] + mul * nums[n - i + j],
                    )

        return max(dp[-1])

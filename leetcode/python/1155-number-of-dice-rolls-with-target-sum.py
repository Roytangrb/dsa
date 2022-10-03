# Author: RT
# Date: 2022-10-02T08:59:34.190Z
# URL: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n:
            return 0

        M = 1_000_000_007
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(i, target + 1):
                for z in range(1, k + 1):
                    if j >= z:
                        dp[i][j] += dp[i - 1][j - z] % M

        return dp[n][target] % M

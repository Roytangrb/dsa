# Author: RT
# Date: 2022-08-01T11:40:49.198Z
# URL: https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

    def uniquePaths__dp_compressed(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for _ in range(m - 2, -1, -1):
            for k in range(n - 2, -1, -1):
                dp[k] += dp[k + 1]

        return dp[0]

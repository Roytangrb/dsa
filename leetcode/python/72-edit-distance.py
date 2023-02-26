# Author: RT
# Date: 2023-02-26T12:49:42.482Z
# URL: https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j], edit distance of word1[i:] and word2[j:]
        # space can be optimized to O(n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case (j=n): delete all
        for i in range(m + 1):
            dp[i][n] = m - i

        # base case (i=m): insert all
        for i in range(n + 1):
            dp[m][i] = n - i

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = (
                    dp[i + 1][j + 1]
                    if word1[i] == word2[j]
                    else min(
                        dp[i][j + 1],  # insert
                        dp[i + 1][j + 1],  # replace
                        dp[i + 1][j],  # delete
                    )
                    + 1
                )

        return dp[0][0]

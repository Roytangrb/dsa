# Author: RT
# Date: 2022-06-14T17:08:37.509Z
# URL: https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[i][j] = lcs of word1[:i] and word2[:j]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    continue
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return m + n - dp[-1][-1] * 2

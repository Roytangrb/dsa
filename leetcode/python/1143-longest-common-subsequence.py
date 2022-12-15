# Author: RT
# Date: 2022-12-15T13:45:06.475Z
# URL: https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """DP compressed O(min(m, n)) memory"""
        m = len(text1)
        n = len(text2)
        if m > n:
            return self.longestCommonSubsequence(text2, text1)

        dp = [0] * (m + 1)
        for i in range(n - 1, -1, -1):
            prev_j_plus_1 = 0
            for j in range(m - 1, -1, -1):
                prev_j = dp[j]
                if text1[j] == text2[i]:
                    dp[j] = prev_j_plus_1 + 1
                else:
                    dp[j] = max(dp[j + 1], prev_j)

                prev_j_plus_1 = prev_j

        return dp[0]

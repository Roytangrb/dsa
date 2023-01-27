# Author: RT
# Date: 2023-01-27T05:12:57.497Z
# URL: https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = frozenset(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))

        return dp[n]

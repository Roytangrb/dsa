# Author: RT
# Date: 2022-06-15T17:07:48.716Z
# URL: https://leetcode.com/problems/longest-string-chain/


from functools import cache


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words_set = set(words)

        @cache
        def dfs(w):
            if not w:
                return 0
            if w not in words_set:
                return 0

            return 1 + max(dfs(w[:i] + w[i + 1 :]) for i in range(len(w)))

        return max(dfs(words[i]) for i in range(len(words)))

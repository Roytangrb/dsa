# Author: RT
# Date: 2022-06-15T17:07:48.716Z
# URL: https://leetcode.com/problems/longest-string-chain/


from functools import cache


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words_set = set(words)

        @cache
        def dfs(w):
            if not w or w not in words_set:
                return 0

            return 1 + max(dfs(w[:i] + w[i + 1 :]) for i in range(len(w)))

        return max(dfs(word) for word in words)

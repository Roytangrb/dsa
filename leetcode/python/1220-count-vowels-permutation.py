# Author: RT
# Date: 2022-08-07T15:20:21.380Z
# URL: https://leetcode.com/problems/count-vowels-permutation/


from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        G = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }
        M = 1_000_000_007

        @cache
        def dp(u, i):
            if i == n:
                return 1

            return sum(dp(v, i + 1) % M for v in G[u]) % M

        return sum(dp(start, 1) % M for start in G.keys()) % M

    def bottom_up(self, n: int, G: dict[str, list[str]], M: int) -> int:
        # dp[c][i] number of permutations starting with char c of length i + 1
        dp = {start: [1] * n for start in G.keys()}

        # conceptually building the string backwards
        ans = 0
        for i in range(1, n):
            for u in G.keys():
                # only previous value of every starting chars is needed, can be
                # further compressed to O(1) space
                dp[u][i] = sum(dp[v][i - 1] for v in G[u]) % M

        return sum(dp[start][-1] for start in G.keys()) % M

# Author: RT
# Date: 2022-10-15T14:30:23.931Z
# URL: https://leetcode.com/problems/string-compression-ii/


from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def dp(idx, last_char, last_char_count, k):
            """Returns cost of compression (compressed length) after handling idx character,
            by either taking the ith character or deleting it"""
            if k < 0:
                return float("inf")
            if idx == n:  # out of bound base case, no extra cost on dp(n-1, ...)
                return 0

            delete_char = dp(idx + 1, last_char, last_char_count, k - 1)
            if s[idx] == last_char:
                keep_char = dp(idx + 1, last_char, last_char_count + 1, k) + (
                    last_char_count in [1, 9, 99]
                )
            else:
                keep_char = dp(idx + 1, s[idx], 1, k) + 1

            return min(keep_char, delete_char)

        return dp(0, "", 0, k)

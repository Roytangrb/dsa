# Author: RT
# Date: 2023-03-03T13:56:12.625Z
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Sliding window"""
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1

# Author: RT
# Date: 2023-07-24T03:28:17.653Z
# URL: https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/


from collections import Counter
from functools import cache


class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        @cache
        def dfs(node):
            """Returns a bit mask of odd frequent characters from node to root"""
            return node and dfs(parent[node]) ^ (1 << (ord(s[node]) - ord("a")))

        cnt = Counter()
        ans, n = 0, len(parent)
        for v in range(n):
            # path u, v (u < v) re-arranged to form palindrome <=>
            # even-length palindrome) for all char, count(u, root) + count(v, root) is even
            # odd-length palindrome) even-length palindrome + 1 extra char as center
            freq = dfs(v)
            ans += cnt[freq]
            ans += sum(cnt[freq ^ (1 << c)] for c in range(26))
            cnt[freq] += 1  # update seen path of u for next v value

        return ans

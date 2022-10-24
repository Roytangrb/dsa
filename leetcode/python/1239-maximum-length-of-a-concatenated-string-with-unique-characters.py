# Author: RT
# Date: 2022-10-24T13:21:13.222Z
# URL: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n = len(arr)
        used = set()

        def backtrack(i, length):
            nonlocal used
            if i == n:
                return length

            ans = 0
            cs = set(arr[i])
            if len(cs) == len(arr[i]) and not (cs & used):
                used |= cs
                ans = backtrack(i + 1, length + len(cs))
                used -= cs

            ans = max(ans, backtrack(i + 1, length))
            return ans

        return backtrack(0, 0)

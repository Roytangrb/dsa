# Author: RT
# Date: 2023-02-04T11:20:40.343Z
# URL: https://leetcode.com/problems/permutation-in-string/


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        total = len(s1)
        charset = Counter(s1)

        n = len(s2)
        l = r = 0

        while r < n and total:
            if charset[s2[r]] > 0:
                charset[s2[r]] -= 1
                total -= 1
                r += 1
                continue

            if l == r:
                l = r = r + 1
                continue

            charset[s2[l]] += 1
            total += 1
            l += 1

        return not total

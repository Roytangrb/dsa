# Author: RT
# Date: 2023-02-05T07:40:29.142Z
# URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        avail = Counter(p)

        l = 0
        for r in range(len(s)):
            if s[r] in avail:
                while l < r and not avail[s[r]]:
                    avail[s[l]] += 1
                    l += 1

                if avail[s[r]]:
                    avail[s[r]] -= 1
            else:  # reset window
                l = r + 1
                avail = Counter(p)

            if r - l + 1 == len(p):
                ans.append(l)

        return ans

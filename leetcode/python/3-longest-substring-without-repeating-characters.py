# Author: RT
# Date: 2022-06-10T14:53:51.183Z
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        ans = 0
        l = 0
        for r, c in enumerate(s):
            if last_seen.get(c, -1) >= l:
                ans = max(ans, r - l)
                l = last_seen[c] + 1

            last_seen[c] = r

        return max(ans, len(s) - l)

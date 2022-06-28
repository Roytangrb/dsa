# Author: RT
# Date: 2022-06-28T13:06:08.388Z
# URL: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        used_freq = float("inf")
        for _, freq in Counter(s).most_common():
            if freq < used_freq:
                used_freq = freq
            else:
                ans += freq - used_freq + 1
                used_freq = max(used_freq - 1, 1)
        return ans

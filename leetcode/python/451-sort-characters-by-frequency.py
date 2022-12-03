# Author: RT
# Date: 2022-12-03T07:47:13.016Z
# URL: https://leetcode.com/problems/sort-characters-by-frequency/


from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(
            c * f
            for c, f in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        )

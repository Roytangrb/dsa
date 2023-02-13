# Author: RT
# Date: 2023-02-13T11:24:26.372Z
# URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1
        n_odd = bool(n & 1)
        return n // 2 + (low & 1) if n_odd else n // 2

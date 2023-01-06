# Author: RT
# Date: 2023-01-06T10:37:44.233Z
# URL: https://leetcode.com/problems/maximum-ice-cream-bars/


from bisect import bisect_right
from itertools import accumulate


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        return bisect_right(list(accumulate(sorted(costs))), coins)

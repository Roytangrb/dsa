# Author: RT
# Date: 2023-03-08T15:32:07.994Z
# URL: https://leetcode.com/problems/koko-eating-bananas/


import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)

        def is_quick_enough(k: int) -> bool:
            t = h
            for p in piles:
                t -= math.ceil(p / k)
                if t < 0:
                    break

            return t >= 0

        r = 0
        s = 0
        for p in piles:
            r = max(r, p)
            s += p

        l = math.ceil(s / h)

        while l < r:
            mid = l + (r - l) // 2
            if is_quick_enough(mid):
                r = mid
            else:
                l = mid + 1

        return l

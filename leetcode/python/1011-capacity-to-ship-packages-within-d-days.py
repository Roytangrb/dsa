# Author: RT
# Date: 2023-02-22T12:55:39.307Z
# URL: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def ok(capacity: int):
            d = 1
            used = 0
            for w in weights:
                if w + used > capacity:
                    if d == days:
                        return False
                    d += 1
                    used = w
                else:
                    used += w

            return d <= days

        l, r = max(weights), sum(weights)
        while l < r:
            capacity = l + (r - l) // 2
            if ok(capacity):
                r = capacity
            else:
                l = capacity + 1

        return r

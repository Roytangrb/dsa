# Author: RT
# Date: 2023-05-23T05:44:26.340Z
# URL: https://leetcode.com/problems/bulb-switcher/


import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Question equals to: Count elements x in [1, n]
        # such that there are odd number of pairs (a, b)
        # using factors of x and a * b = x.
        # Only perfect square will have odd number of factor pairs
        return int(math.sqrt(n))

    def bulbSwitch__brute_force(self, n: int) -> int:
        statuses = [False] * n
        for r in range(1, n + 1):
            for b in range(1, n + 1):
                # toggle when b % r == 0
                if b % r == 0:
                    statuses[b - 1] = not statuses[b - 1]

        return sum(statuses)

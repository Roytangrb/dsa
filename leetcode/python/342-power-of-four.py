# Author: RT
# Date: 2022-08-22T14:21:20.356Z
# URL: https://leetcode.com/problems/power-of-four/


import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n is not 0 and n has only 1 set bit and leftshifted by multiple of 2
        return bool(n) and n == n & ~(n - 1) and math.log2(n) % 2 == 0

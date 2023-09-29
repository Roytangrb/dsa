# Author: RT
# Date: 2023-09-29T02:47:21.999Z
# URL: https://leetcode.com/problems/the-kth-factor-of-n/

import math
from collections import deque


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """O(sqrt(n))"""
        # store counterpart of factor <= sqrt(n) in asc order
        factors = deque()
        for i in range(1, int(math.sqrt(n)) + 1):
            q, r = divmod(n, i)
            if r == 0:
                k -= 1
                if q != i:
                    # q * i = n where q > i
                    factors.appendleft(q)

            if k == 0:
                return i

        if k > 0 and k - 1 < len(factors):
            return factors[k - 1]

        return -1


class Solution_brute_force:
    def kthFactor(self, n: int, k: int) -> int:
        """O(n)"""
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i

        return -1

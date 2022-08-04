# Author: RT
# Date: 2022-08-04T14:31:55.149Z
# URL: https://leetcode.com/problems/mirror-reflection/


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        h = v = 1
        while p * h != q * v:
            v += 1
            h = q * v // p

        odd = lambda x: bool(x & 1)
        even = lambda x: not odd(x)

        if odd(h) and even(v):
            return 2
        if odd(h) and odd(v):
            return 1
        if even(h) and odd(v):
            return 0

        return -1

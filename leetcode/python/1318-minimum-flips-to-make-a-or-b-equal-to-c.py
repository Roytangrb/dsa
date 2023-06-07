# Author: RT
# Date: 2023-06-07T03:42:13.799Z
# URL: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            ba = a & 1
            bb = b & 1
            bc = c & 1
            if ba | bb != bc:
                if bc:
                    ans += 1
                else:
                    ans += bool(ba) + bool(bb)

            a >>= 1
            b >>= 1
            c >>= 1

        return ans

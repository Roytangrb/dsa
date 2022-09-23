# Author: RT
# Date: 2022-09-23T05:34:51.282Z
# URL: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        M = 1_000_000_007
        ans = 0
        offset = 0  # cumulative offset before concat
        for num in range(1, n + 1):
            # whenever num becomes power of 2, the offset to shift will
            # increase by 1, check if num is power of 2
            if num & (num - 1) == 0:
                offset += 1

            ans = (ans << offset | num) % M

        return ans % M

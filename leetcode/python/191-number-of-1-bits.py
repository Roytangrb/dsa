# Author: RT
# Date: 2022-05-26T15:59:26.741Z
# URL: https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n - 1
            ans += 1

        return ans

# Author: RT
# Date: 2022-12-12T13:32:37.114Z
# URL: https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        p2 = p1 = 1
        for i in range(2, n + 1):
            p1, p2 = p1 + p2, p1

        return p1

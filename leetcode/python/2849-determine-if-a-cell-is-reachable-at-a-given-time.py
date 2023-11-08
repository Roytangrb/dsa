# Author: RT
# Date: 2023-11-08T03:33:51.840Z
# URL: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diff_x = abs(fx - sx)
        diff_y = abs(fy - sy)
        if not diff_x and not diff_y:
            return t != 1

        return t >= max(diff_x, diff_y)

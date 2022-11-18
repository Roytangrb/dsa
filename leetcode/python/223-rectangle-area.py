# Author: RT
# Date: 2022-11-18T14:53:41.127Z
# URL: https://leetcode.com/problems/rectangle-area/


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # one dimension
        # a ----------- b
        #          c ---------- d
        # overlap = max(min(b, d) - max(a, c), 0)

        overlap_x = max(min(ax2, bx2) - max(ax1, bx1), 0)
        overlap_y = max(min(ay2, by2) - max(ay1, by1), 0)

        return (
            (ax2 - ax1) * (ay2 - ay1)
            + (bx2 - bx1) * (by2 - by1)
            - overlap_x * overlap_y
        )

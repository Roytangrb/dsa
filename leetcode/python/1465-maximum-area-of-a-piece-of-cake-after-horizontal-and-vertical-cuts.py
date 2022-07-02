# Author: RT
# Date: 2022-07-02T17:07:35.650Z
# URL: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]
    ) -> int:
        M = 10**9 + 7

        prev = 0
        max_w = 0
        for j in sorted(verticalCuts):
            max_w = max(max_w, j - prev)
            prev = j
        max_w = max(max_w, w - prev)

        prev = 0
        max_h = 0
        for i in sorted(horizontalCuts):
            max_h = max(max_h, i - prev)
            prev = i
        max_h = max(max_h, h - prev)

        return (max_w * max_h) % M

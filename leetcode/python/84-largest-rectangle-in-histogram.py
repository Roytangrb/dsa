# Author: RT
# Date: 2022-11-25T14:49:00.218Z
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

from itertools import chain


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        ans = 0
        for i, h in enumerate(chain(heights, [0])):
            while stack[-1] > -1 and h <= heights[stack[-1]]:
                cur_h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, w * cur_h)
            stack.append(i)

        return ans

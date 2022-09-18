# Author: RT
# Date: 2022-09-18T12:25:14.156Z
# URL: https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        highest_l = [0] * n
        highest_r = [0] * n
        ans = 0

        for i in range(1, n):
            highest_l[i] = max(highest_l[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            highest_r[i] = max(highest_r[i + 1], height[i + 1])

        for i, h in enumerate(height):
            gain = max(min(highest_l[i], highest_r[i]) - h, 0)
            ans += gain
        return ans

    def trap__stack(self, height: list[int]) -> int:
        stack = []
        ans = 0
        for r, h in enumerate(height):
            while stack and stack[-1][0] < h:
                bar_h, bar_i = stack.pop()
                if not stack:
                    break
                lh, l = stack[-1]
                ans += (min(lh, h) - bar_h) * (r - l - 1)

            stack.append((h, r))

        return ans

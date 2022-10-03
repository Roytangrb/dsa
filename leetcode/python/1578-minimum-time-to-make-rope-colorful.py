# Author: RT
# Date: 2022-10-03T14:55:37.892Z
# URL: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        running_sum = 0
        running_cnt = 0
        running_max = 0
        ans = 0
        prev_color = ""
        for c, t in zip(colors, neededTime):
            if c == prev_color:
                running_sum += t
                running_cnt += 1
                running_max = max(running_max, t)
            else:
                prev_color = c
                ans += running_sum - running_max
                running_sum = t
                running_cnt = 1
                running_max = t

        return ans + (running_sum - running_max if running_cnt > 1 else 0)

# Author: RT
# Date: 2023-08-13T20:19:34.818Z
# URL: https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/


from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        n = len(nums)
        sl = SortedList(nums[x:])
        ans = float("inf")
        for i in range(n - x):
            best = sl.bisect_right(nums[i])
            if best < len(sl):
                ans = min(ans, abs(sl[best] - nums[i]))
            if best - 1 >= 0:
                ans = min(ans, abs(sl[best - 1] - nums[i]))
            if best + 1 < len(sl):
                ans = min(ans, abs(sl[best + 1] - nums[i]))

            sl.pop(sl.index(nums[i + x]))

        return ans

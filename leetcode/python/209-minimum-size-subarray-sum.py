# Author: RT
# Date: 2023-07-06T05:51:47.728Z
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/description/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l = s = ans = 0
        for r in range(n):
            s += nums[r]
            while s >= target:
                ans = min(ans or n, r - l + 1)
                s -= nums[l]
                l += 1

        return ans

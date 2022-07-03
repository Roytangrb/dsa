# Author: RT
# Date: 2022-07-03T16:59:38.755Z
# URL: https://leetcode.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        prev_diff = nums[1] - nums[0]
        ans = 1 if not prev_diff else 2
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                ans += 1
                prev_diff = diff

        return ans

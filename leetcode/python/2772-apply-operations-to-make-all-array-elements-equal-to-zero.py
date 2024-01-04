# Author: RT
# Date: 2023-07-09T05:56:13.462Z
# URL: https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/


class Solution:
    def checkArray(self, nums: list[int], k: int) -> bool:
        # accrued value need to be deleted from window ending at current index
        # as we slide the window from left to right
        curr = 0
        n = len(nums)
        for i in range(n):
            if curr > nums[i]:
                return False

            nums[i], curr = nums[i] - curr, nums[i]
            if i + 1 >= k:
                curr -= nums[i - k + 1]

        return curr == 0

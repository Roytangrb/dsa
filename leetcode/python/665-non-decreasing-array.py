# Author: RT
# Date: 2022-06-25T13:58:13.947Z
# URL: https://leetcode.com/problems/non-decreasing-array/


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            a = nums[l + 1] >= nums[l]
            b = nums[r - 1] <= nums[r]
            if a:
                l += 1
            if b:
                r -= 1
            if not a and not b:
                break
            if r - l == 1:
                if l == 0 or nums[l - 1] <= nums[r]:
                    return True
                if r == n - 1 or nums[r + 1] >= nums[l]:
                    return True
                return False
        return r - l <= 1

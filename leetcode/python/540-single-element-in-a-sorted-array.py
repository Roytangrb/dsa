# Author: RT
# Date: 2023-02-21T13:49:14.337Z
# URL: https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            # odd xor 1 = odd - 1
            # even xor 1 = even + 1
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid

        return nums[r]

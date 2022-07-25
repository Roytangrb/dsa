# Author: RT
# Date: 2022-07-25T14:23:15.995Z
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ans = [-1, -1]
        if not nums:
            return ans

        # find leftmost target
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2  # biased towards left
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        ans[0] = l if nums[l] == target else -1

        # find rightmost target
        l, r = 0, n - 1
        while l < r:
            mid = (r + l + 1) // 2  # biased towards right
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid

        ans[1] = r if nums[r] == target else -1

        return ans

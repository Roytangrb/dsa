# Author: RT
# Date: 2022-06-22T14:21:54.515Z
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def quickselect(l, r):
            ptr = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]

            if ptr == n - k:
                return nums[ptr]
            elif ptr < n - k:
                return quickselect(ptr + 1, r)
            else:
                return quickselect(l, ptr - 1)

        return quickselect(0, n - 1)

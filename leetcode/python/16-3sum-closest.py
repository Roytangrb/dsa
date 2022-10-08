# Author: RT
# Date: 2022-10-08T11:36:31.019Z
# URL: https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = sum(nums[:3])

        for i in range(n - 2):
            ret = nums[i] + self.twoSumClosest(nums, i + 1, target - nums[i])
            if ret == target:
                return target

            if abs(ret - target) <= abs(ans - target):
                ans = ret

        return ans

    def twoSumClosest(self, nums: list[int], i: int, target: int) -> int:
        l = i
        r = len(nums) - 1
        ans = nums[l] + nums[r]

        while l < r:
            ret = nums[l] + nums[r]
            if ret == target:
                return target
            elif ret < target:
                l += 1
            else:
                r -= 1
            if abs(ret - target) <= abs(ans - target):
                ans = ret

        return ans

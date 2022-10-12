# Author: RT
# Date: 2022-10-12T14:54:04.745Z
# URL: https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        # a > b > c
        a, b = nums[-1], nums[-2]
        for ci in range(n - 3, -1, -1):
            c = nums[ci]
            if c + b > a:
                return a + b + c
            else:
                a, b = b, c

        return 0

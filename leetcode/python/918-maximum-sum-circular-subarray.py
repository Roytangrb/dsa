# Author: RT
# Date: 2023-01-18T16:37:12.611Z
# URL: https://leetcode.com/problems/maximum-sum-circular-subarray/


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Max circular subarray sum = max(max sum subrray, total - min sum subarray)"""
        total = 0
        max_sum = float("-inf")
        min_sum = float("inf")
        max_run = min_run = 0
        for num in nums:
            total += num

            max_run += num
            max_sum = max(max_sum, max_run)
            max_run = max(max_run, 0)

            min_run += num
            min_sum = min(min_sum, min_run)
            min_run = min(min_run, 0)

        if min_sum == total:
            return max_sum

        return max(max_sum, total - min_sum)

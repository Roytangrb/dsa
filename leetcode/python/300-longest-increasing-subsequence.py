# Author: RT
# Date: 2022-07-17T11:01:19.180Z
# URL: https://leetcode.com/problems/longest-increasing-subsequence/


import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """Patience sort"""
        n = len(nums)
        tails = [nums[0]]

        for i in range(1, n):
            if nums[i] > tails[-1]:
                # extend the current longest LIS
                tails.append(nums[i])
            else:
                # exisiting length of LIS is found, replace end element with smaller value
                tails[bisect.bisect_left(tails, nums[i])] = nums[i]

        return len(tails)

    def lengthOfLIS__dp(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

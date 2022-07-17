# Author: RT
# Date: 2022-05-25T16:42:12.313Z
# URL: https://leetcode.com/problems/russian-doll-envelopes/

import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """Patience sort"""
        # convert problem to longest increasing subsequence (LIS) size
        # sort h desc so that evelopes with same w cannot be in the same sequence
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [d[1] for d in envelopes]

        # Ref: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        n = len(nums)
        # storing the tail element of active lists only coz we only need LIS size
        tails = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if num < tails[0]:
                tails[0] = num
            elif num > tails[-1]:
                tails.append(num)
            else:
                tails[bisect.bisect_left(tails, num)] = num

        return len(tails)

    def maxEnvelopes__dp(self, envelopes: list[list[int]]) -> int:
        # convert problem to longest increasing subsequence (LIS) size
        # sort h desc so that evelopes with same w cannot be in the same sequence
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [d[1] for d in envelopes]

        # longest subsequence ending at i
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

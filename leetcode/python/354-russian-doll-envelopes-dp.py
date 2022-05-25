# Author: RT
# Date: 2022-05-25T16:45:12.953Z
# URL: https://leetcode.com/problems/russian-doll-envelopes/


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
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

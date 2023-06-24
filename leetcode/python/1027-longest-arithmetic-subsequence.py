# Author: RT
# Date: 2023-06-23T03:35:06.714Z
# URL: https://leetcode.com/problems/longest-arithmetic-subsequence/


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        # dp[ending index][diff], use dict for sparse & possibly negative diff values
        dp, n = {}, len(nums)
        for r in range(n):
            for l in range(r):
                diff = nums[r] - nums[l]
                dp[(r, diff)] = dp.get((l, diff), 1) + 1

        return max(dp.values())

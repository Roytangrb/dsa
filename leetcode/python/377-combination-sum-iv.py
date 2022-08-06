# Author: RT
# Date: 2022-08-06T14:41:45.764Z
# URL: https://leetcode.com/problems/combination-sum-iv/


from functools import cache


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @cache
        def dp(x):
            ans = 0

            for num in nums:
                if num == x:
                    ans += 1
                elif num < x:
                    ans += dp(x - num)

            return ans

        return dp(target)

    def bottom_up(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # when the last number equals to target

        for x in range(1, target + 1):
            for num in nums:
                if num <= x:
                    dp[x] += dp[x - num]

        return dp[target]

# Author: RT
# Date: 2022-12-14T13:15:54.039Z
# URL: https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        robbed = skipped = 0
        for num in nums:
            robbed, skipped = max(robbed, skipped + num), max(robbed, skipped)

        return max(skipped, robbed)

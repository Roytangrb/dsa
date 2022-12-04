# Author: RT
# Date: 2022-12-04T06:26:45.961Z
# URL: https://leetcode.com/problems/minimum-average-difference/


from itertools import accumulate


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = accumulate(nums)
        total = sum(nums)

        return (
            min(
                enumerate(prefix, 1),
                key=lambda x: abs(
                    x[1] // x[0] - (total - x[1]) // (n - x[0] if x[0] < n else 1)
                ),
            )[0]
            - 1
        )

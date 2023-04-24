# Author: RT
# Date: 2023-03-21T13:54:01.783Z
# URL: https://leetcode.com/problems/number-of-zero-filled-subarrays/


from itertools import chain


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        l = ans = 0
        for r, num in enumerate(chain(nums, [1])):
            if num != 0:
                k = r - l
                ans += (k + 1) * k // 2
                l = r + 1

        return ans

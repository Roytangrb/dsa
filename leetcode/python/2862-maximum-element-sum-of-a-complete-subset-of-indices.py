# Author: RT
# Date: 2023-09-17T18:01:48.464Z
# URL: https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

from collections import Counter


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        # Square factorization: for every index i, divide by all perfect square
        # numbers which are factors of i, the remainder is considered the 'key'.
        # If 2 indices have the same 'key', the multiply result of them is also
        # a perfect square.
        # Algorithm:
        #   1. find key of all indices
        #   2. group indices by key and maintain running sum of nums[i] within
        #      each group, update ans
        group_sum = Counter()
        for i, num in enumerate(nums, 1):  # index starting from 1
            step = 2
            while i >= (perf_sqr := step * step):
                while i % perf_sqr == 0:
                    i //= perf_sqr

                step += 1

            group_sum[i] += num

        return max(group_sum.values())

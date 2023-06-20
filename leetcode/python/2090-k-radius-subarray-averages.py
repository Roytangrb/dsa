# Author: RT
# Date: 2023-06-20T03:08:30.608Z
# URL: https://leetcode.com/problems/k-radius-subarray-averages/


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        n = len(nums)
        win_sum = 0
        avgs = [-1] * n
        for i in range(n):
            win_sum += nums[i]
            if i < 2 * k:
                continue

            avgs[i - k] = win_sum // (2 * k + 1)
            win_sum -= nums[i - 2 * k]

        return avgs

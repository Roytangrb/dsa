# Author: RT
# Date: 2023-07-21T00:18:29.131Z
# URL: https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        length = [1] * n  # length of LIS ending at index i
        count = [1] * n  # count of LIS ending at index i
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:  # new LIS length
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        lis_length = max(length)

        return sum(c for l, c in zip(length, count) if l == lis_length)

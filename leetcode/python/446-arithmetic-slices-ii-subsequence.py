# Author: RT
# Date: 2022-11-27T14:34:34.317Z
# URL: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/


from collections import Counter


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = [Counter() for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                s = 0
                if delta in cnt[j]:
                    s = cnt[j][delta]
                cnt[i][delta] += s + 1
                ans += s

        return ans

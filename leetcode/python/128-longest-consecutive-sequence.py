# Author: RT
# Date: 2022-07-05T12:07:52.506Z
# URL: https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                start = num
                count = 1
                while start + 1 in num_set:
                    start += 1
                    count += 1

                ans = max(ans, count)

        return ans

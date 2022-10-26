# Author: RT
# Date: 2022-10-26T14:30:20.963Z
# URL: https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        s = 0
        seen = {0: -1}  # mod k: leftmost position
        for i, num in enumerate(nums):
            s += num
            m = s % k
            if m in seen and i - seen[m] > 1:
                return True

            if m not in seen:
                seen[m] = i

        return False

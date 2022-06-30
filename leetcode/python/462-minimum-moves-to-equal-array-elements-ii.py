# Author: RT
# Date: 2022-06-30T15:27:13.502Z
# URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        # Optmization: use partial sort (quickselect) to find median
        mid = nums[n // 2]
        for num in nums:
            ans += abs(mid - num)
        return ans

# Author: RT
# Date: 2023-02-20T12:58:54.877Z
# URL: https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n

        # bisect right
        while l < r:
            mid = l + (r - l) // 2
            if (curr := nums[mid]) == target:
                return mid
            elif curr > target:
                r = mid
            else:
                l = mid + 1

        return r

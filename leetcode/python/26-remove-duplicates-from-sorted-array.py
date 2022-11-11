# Author: RT
# Date: 2022-11-11T15:45:12.614Z
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        insert = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[insert] = nums[i]
                insert += 1

        return insert

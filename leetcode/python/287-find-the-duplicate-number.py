# Author: RT
# Date: 2022-06-06T15:20:15.431Z
# URL: https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Author: RT
# Date: 2022-10-21T13:33:36.252Z
# URL: https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True

            last_seen[num] = i

        return False

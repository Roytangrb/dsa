# Author: RT
# Date: 2022-10-23T07:41:13.566Z
# URL: https://leetcode.com/problems/set-mismatch/


class Solution:
    def findErrorNums__set(self, nums: list[int]) -> list[int]:
        """O(n) space using hash set"""
        n = len(nums)
        s = 0
        seen = set()
        dup = 0
        for num in nums:
            s += num
            if num in seen:
                dup = num

            seen.add(num)

        return [dup, (1 + n) * n // 2 - s + dup]

    def findErrorNums__flag_inplace(self, nums: list[int]) -> list[int]:
        """Mark dirty using num [1, n) as index"""
        n = len(nums)
        dup = 0
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                dup = abs(num)
            else:
                nums[i] *= -1

        missing = next(i for i in range(n) if nums[i] > 0) + 1
        return [dup, missing]

    def findErrorNums__xor(self, nums: list[int]) -> list[int]:
        dup_xor_missing = 0
        for i, num in enumerate(nums):
            dup_xor_missing ^= (i + 1) ^ num

        # pick a bit that duplicate and missing differs in
        rightmost_set_bit = dup_xor_missing & ~(dup_xor_missing - 1)
        # split original nums and current nums into 2 set, one group
        # with the target bit set, the other without
        # in both groups, after cancelling out number appearing twice
        # duplicate and missing will remain in one of the groups respectively
        xor1 = xor0 = 0
        for i, num in enumerate(nums):
            if (i + 1) & rightmost_set_bit:
                xor1 ^= i + 1
            else:
                xor0 ^= i + 1

            if num & rightmost_set_bit:
                xor1 ^= num
            else:
                xor0 ^= num

        return [xor0, xor1] if xor0 in nums else [xor1, xor0]

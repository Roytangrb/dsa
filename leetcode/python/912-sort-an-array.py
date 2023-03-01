# Author: RT
# Date: 2023-03-01T13:55:33.750Z
# URL: https://leetcode.com/problems/sort-an-array/


import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """Quicksort worst-case O(n2)"""
        def qs(l: int, r: int):
            if l >= r:
                return
            
            # median of 3
            # x = l + (r - l) // 2  # left median
            # pivot = sorted([l, x, r], key=lambda i: nums[i])[1]
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[r] = nums[r], nums[i]
            qs(l, i)
            qs(i+1, r)

        qs(0, len(nums)-1)
        
        return nums


# Author: RT
# Date: 2023-09-30T03:09:04.921Z
# URL: https://leetcode.com/problems/132-pattern/


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        i = nums[0]
        for k in nums:
            while stack and k >= stack[-1][0]:
                # nums pop from stack are to the left of nums remaining in stack
                i = min(i, stack.pop()[0])

            # if stack is not empty, nums[k] < nums[j] exists
            # check if the current num greater that min value
            # to the left of j, if so nums[k] < nums[i] exists
            if stack and stack[-1][1] < k:
                return True

            stack.append((k, i))

        return False

# Author: RT
# Date: 2023-08-16T05:52:25.788Z
# URL: https://leetcode.com/problems/sliding-window-maximum/description/


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        win = deque()
        ans = []

        for i, num in enumerate(nums):
            while win and nums[win[-1]] <= num:
                win.pop()

            win.append(i)
            if win[0] == i - k:
                win.popleft()
            if i >= k - 1:
                ans.append(nums[win[0]])

        return ans

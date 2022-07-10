# Author: RT
# Date: 2022-07-09T18:02:41.570Z
# URL: https://leetcode.com/problems/jump-game-vi/

from collections import deque


class Solution:
    def maxResult__mono_queue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        # use monotonic deque to keep track of max values in sliding window
        window = deque()

        for i, num in enumerate(nums):
            while window and window[0] < i - k:
                window.popleft()

            dp[i] = dp[window[0]] + num if window else num

            while window and dp[window[-1]] < dp[i]:
                window.pop()

            window.append(i)

        return dp[-1]

    def maxResult__mono_queue_compressed(self, nums: list[int], k: int) -> int:
        """O(k) memory, at each step only previous score within the window needs
        to be considered"""
        n = len(nums)
        # (sum of score, index used)
        window: deque[tuple[int, int]] = deque([(nums[0], 0)])

        for i in range(1, n):
            while window[0][1] < i - k:
                window.popleft()

            curr = window[0][0] + nums[i]

            while window and window[-1][0] <= curr:
                window.pop()

            window.append((curr, i))

        return window[-1][0]

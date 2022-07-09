# Author: RT
# Date: 2022-07-09T18:02:41.570Z
# URL: https://leetcode.com/problems/jump-game-vi/

from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
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

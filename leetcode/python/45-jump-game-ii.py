# Author: RT
# Date: 2023-02-08T14:03:29.381Z
# URL: https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: list[int]) -> int:
        # Greedy O(n)
        n = len(nums)
        ans = 0
        l, r = 0, 1  # r = farthest position reachable after each jump
        while r < n:
            l, r = r, max(i + nums[i] for i in range(l, r)) + 1
            ans += 1

        return ans

    def jump__dp(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0
        for i in reversed(range(n - 1)):
            dp[i] = min(dp[i : min(n, i + nums[i] + 1)], default=float("inf")) + 1

        return dp[0]

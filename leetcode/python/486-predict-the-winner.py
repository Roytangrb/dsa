# Author: RT
# Date: 2023-07-28T04:10:32.283Z
# URL: https://leetcode.com/problems/predict-the-winner/description/


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        # if nums is even-length, p1 always wins
        if not n & 1:
            return True

        # dp[l][r] p1 score - p2 score playing with nums[l:r+1]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        # fill dp diagonally
        for offset in range(1, n):
            for l in range(n - offset):
                r = l + offset
                dp[l][r] = max(nums[l] - dp[l + 1][r], nums[r] - dp[l][r - 1])

        return dp[0][-1] >= 0

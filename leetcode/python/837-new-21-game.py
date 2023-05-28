# Author: RT
# Date: 2023-05-27T19:51:36.676Z
# URL: https://leetcode.com/problems/new-21-game/


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Optimize second loop with sliding window sum"""
        if k + maxPts - 1 <= n or k == 0:
            return 1

        # dp[i], the probability of ending the game with number i
        m = min(n + 1, k + maxPts)
        dp = [0.0] * m
        dp[0] = 1
        prob = 1 / maxPts
        # sum of probability in window
        window_prob = 1
        ans = 0
        for i in range(1, m):
            dp[i] = window_prob * prob
            # increase window right unless the game stopped at i
            if i < k:
                window_prob += dp[i]
            else:
                ans += dp[i]
            # shrink window on the left
            if i >= maxPts:
                window_prob -= dp[i - maxPts]

        return ans

    def new21Game__brute_force(self, n: int, k: int, maxPts: int) -> float:
        # TLE
        if k + maxPts - 1 <= n or k == 0:
            return 1

        # dp[i], the probability of ending the game with number i
        m = min(n + 1, k + maxPts)
        dp = [0.0] * m
        prob = 1 / maxPts
        dp[0] = 1
        for i in range(1, m):
            for prev_draw in range(1, maxPts + 1):
                prev_score = i - prev_draw
                if prev_score >= 0 and prev_score < k:
                    dp[i] += dp[prev_score] * prob

        return sum(dp[k:])

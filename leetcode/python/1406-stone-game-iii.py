# Author: RT
# Date: 2023-06-01T04:56:00.508Z
# URL: https://leetcode.com/problems/stone-game-iii/


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # When the game start at i, dp[i] is the score of
        # first player - score of second player
        dp = [0] * (n + 1)
        for i in reversed(range(0, n)):
            # take 1 stone
            # NOTE: denote the current player as X, because the players takes turn
            # to play, the next dp state represents the opponent's score - the
            # current player's own score.
            dp[i] = stoneValue[i] - dp[i + 1]
            # take 2 stone
            if i + 1 < n:
                dp[i] = max(dp[i], sum(stoneValue[i : i + 2]) - dp[i + 2])
            # take 3 stone
            if i + 2 < n:
                dp[i] = max(dp[i], sum(stoneValue[i : i + 3]) - dp[i + 3])

        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"

    def stoneGameIII__space_optimized(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = (0, None, None)
        for i in reversed(range(0, n)):
            curr = stoneValue[i] - dp[0]
            if dp[1] is not None:
                curr = max(curr, sum(stoneValue[i : i + 2]) - dp[1])
            if dp[2] is not None:
                curr = max(curr, sum(stoneValue[i : i + 3]) - dp[2])

            dp = curr, dp[0], dp[1]

        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"

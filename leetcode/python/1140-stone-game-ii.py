# Author: RT
# Date: 2023-05-28T04:14:41.468Z
# URL: https://leetcode.com/problems/stone-game-ii/

from functools import cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        @cache
        def dp(player, i, m):
            if i == n:
                return 0

            ans = 0 if player == 0 else 1_000_000
            prefix_sum = 0
            for x in range(1, min(2 * m, n - i) + 1):
                prefix_sum += piles[i + x - 1]
                if player == 0:  # Alice
                    ans = max(ans, prefix_sum + dp(1, i + x, max(x, m)))
                else:  # Bob
                    ans = min(ans, dp(0, i + x, max(x, m)))

            return ans

        return dp(0, 0, 1)

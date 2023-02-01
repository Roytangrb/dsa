# Author: RT
# Date: 2023-01-31T15:49:06.750Z
# URL: https://leetcode.com/problems/best-team-with-no-conflicts/


from functools import cache


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        n = len(scores)
        age_score = sorted(zip(ages, scores))

        @cache
        def dp(i: int, max_score: int) -> int:
            if i == n:
                return 0

            _, score = age_score[i]
            if score >= max_score:
                return max(
                    dp(i + 1, score) + score,
                    dp(i + 1, max_score),
                )

            return dp(i + 1, max_score)

        return dp(0, 0)

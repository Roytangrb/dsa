# Author: RT
# Date: 2022-10-16T12:56:22.510Z
# URL: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/


from functools import cache


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        suffix_max = list(jobDifficulty)
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], jobDifficulty[i])

        @cache
        def dp(first_job: int, remaining_days: int) -> int | float:
            if remaining_days == 1:
                return suffix_max[first_job]

            day_difficulty = jobDifficulty[first_job]
            min_difficulty = float("inf")
            for job in range(first_job + 1, n):
                day_difficulty = max(day_difficulty, jobDifficulty[job - 1])
                min_difficulty = min(
                    min_difficulty, dp(job, remaining_days - 1) + day_difficulty
                )

            return min_difficulty

        if d > n:
            return -1

        ans = dp(0, d)
        return ans if ans != float("inf") else -1

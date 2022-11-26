# Author: RT
# Date: 2022-11-26T16:01:47.907Z
# URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling/


from bisect import bisect_left


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        """0-1 Knapsack Problem"""
        n = len(profit)
        jobs = sorted(zip(startTime, endTime, profit))
        dp = [0] * (n + 1)  # dp[i] is max total profit by scheduling jobs[i:]

        for i in reversed(range(n)):
            _, end, w = jobs[i]
            # find earliest start time if current job scheduled
            j = bisect_left(jobs, end, lo=i, key=lambda j: j[0])
            dp[i] = max(
                dp[i + 1],  # exclude current job
                dp[j] + w,  # include current job
            )

        return dp[0]

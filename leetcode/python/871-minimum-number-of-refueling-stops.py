# Author: RT
# Date: 2022-08-20T17:23:41.986Z
# URL: https://leetcode.com/problems/minimum-number-of-refueling-stops/


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: list[list[int]]
    ) -> int:
        # the farthest location we can get to using i refueling stops.
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel

        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        return next((i for i, d in enumerate(dp) if d >= target), -1)

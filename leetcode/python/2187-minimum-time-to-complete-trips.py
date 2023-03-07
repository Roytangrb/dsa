# Author: RT
# Date: 2023-03-07T15:17:33.603Z
# URL: https://leetcode.com/problems/minimum-time-to-complete-trips/


import bisect


class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        time.sort()
        n = len(time)

        def trips_with_t(t: int) -> int:
            trips = 0
            for i in range(n):
                if time[i] > t:
                    break

                trips += t // time[i]

            return trips

        class TRange:
            def __getitem__(self, t) -> int:
                return trips_with_t(t)

        return bisect.bisect_left(TRange(), totalTrips, lo=0, high=time[0] * totalTrips)

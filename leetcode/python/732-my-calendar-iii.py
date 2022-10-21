# Author: RT
# Date: 2022-10-21T15:25:23.261Z
# URL: https://leetcode.com/problems/my-calendar-iii/


from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        # {[time t]: delta of overlap count at time t}
        self.delta = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1

        ans = 0
        cnt = 0
        for d in self.delta.values():
            cnt += d
            ans = max(ans, cnt)

        return ans

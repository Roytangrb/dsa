# Author: RT
# Date: 2023-01-28T07:00:40.683Z
# URL: https://leetcode.com/problems/data-stream-as-disjoint-intervals/


from sortedcontainers import SortedList


class SummaryRanges:
    def __init__(self):
        self.values = SortedList()

    def addNum(self, value: int) -> None:
        if value not in self.values:
            self.values.add(value)

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        interval = []
        for v in self.values:
            if not interval:
                interval = [v, v]
            elif interval[1] + 1 == v:
                interval[1] = v
            else:
                intervals.append(interval)
                interval = [v, v]

        if interval:
            intervals.append(interval)

        return intervals

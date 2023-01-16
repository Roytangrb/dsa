# Author: RT
# Date: 2023-01-16T14:39:21.188Z
# URL: https://leetcode.com/problems/insert-interval/


from bisect import bisect_left, bisect_right


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        start, end = newInterval
        n = len(intervals)
        l = bisect_left(intervals, start, key=lambda x: x[1])
        r = bisect_right(intervals, end, key=lambda x: x[0])

        front = intervals[:l]
        rear = intervals[r:]
        merged = [
            min(intervals[l][0], start) if l < n else start,
            max(intervals[r - 1][1], end) if r > 0 else end,
        ]

        return front + [merged] + rear

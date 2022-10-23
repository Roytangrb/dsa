# Author: RT
# Date: 2022-10-21T15:25:23.261Z
# URL: https://leetcode.com/problems/my-calendar-iii/


from collections import Counter

from sortedcontainers import SortedDict, SortedList


class MyCalendarThree:
    """O(n) Sweep-line algorithm"""

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


class MyCalendarThreeSegmentTree:
    """O(nlogC) with segment tree where n = no. of book calls, C = max event time range"""

    def __init__(self):
        # events are sparsed in the [0, 1e9], store only segments that
        # have values using hashmap
        # vals: max number of overlaps within [start, end)
        # When parent segment with id = idx
        # Left child = segment [start, mid], id = idx * 2
        # Right child = segment [mid+1, end-1], id = idx * 2 + 1
        # i.e., vals[1] = answer, i.e. max number of overlaps within [0, 1e9]
        # i.e., vals[2] = answer, i.e. max number of overlaps within [0, 1e9 // 2]
        # i.e., vals[3] = answer, i.e. max number of overlaps within [1e9 // 2 + 1, 1e9]
        self.vals = Counter()
        # vals[idx] = shared[idx] + max(vals[idx * 2], vals[idx * 2 + 1])
        # shared[idx] represents count of events that cover the full range of segment idx
        # i.e. lazy count that are not propagate to children's vals but counted upon query
        self.shared = Counter()

    def update(
        self,
        event_start: int,
        event_end: int,
        seg_left: int = 0,
        seg_right: int = 10**9,
        segment_id: int = 1,
    ):
        if event_end < seg_left or event_start > seg_right:
            return

        if event_start <= seg_left <= seg_right <= event_end:
            # event cover the whole segment, update shared count for children segments
            self.vals[segment_id] += 1
            self.shared[segment_id] += 1
        else:
            mid = (seg_left + seg_right) // 2
            self.update(event_start, event_end, seg_left, mid, segment_id * 2)
            self.update(event_start, event_end, mid + 1, seg_right, segment_id * 2 + 1)
            self.vals[segment_id] = self.shared[segment_id] + max(
                self.vals[segment_id * 2], self.vals[segment_id * 2 + 1]
            )

    def book(self, startTime: int, endTime: int) -> int:
        # 0 <= startTime <= endTime <= 1e9
        self.update(startTime, endTime - 1)
        return self.vals[1]


class MyCalendarThreeBalancedTree:
    """Split range with balanced tree (Chtholly Tree)

    O(n2) worst case when every event covers all previous events.
    https://docs.rs/chtholly_tree/latest/chtholly_tree/
    """

    def __init__(self):
        self.stops = SortedList([0, 10**9])
        self.counts = Counter()
        self.max_count = 0

    def split(self, stop: int):
        """Split range by adding a stop if not exists"""
        idx = self.stops.bisect_left(stop)
        if stop != self.stops[idx]:
            self.counts[stop] = self.counts[self.stops[idx - 1]]
            self.stops.add(stop)

    def book(self, startTime: int, endTime: int) -> int:
        """Split the range [0, 1e9] into smaller intervals after adding a new event
        increment count of split intervals between [start, end)."""
        self.split(startTime)
        self.split(endTime)
        for stop in self.stops.irange(startTime, endTime, inclusive=(True, False)):
            self.counts[stop] += 1
            self.max_count = max(self.max_count, self.counts[stop])

        return self.max_count

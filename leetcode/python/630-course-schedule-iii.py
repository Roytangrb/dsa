# Author: RT
# Date: 2022-06-25T15:21:40.709Z
# URL: https://leetcode.com/problems/course-schedule-iii/

import heapq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        pq = []
        total = 0
        for t, end in sorted(courses, key=lambda d: d[1]):
            total += t
            heapq.heappush(pq, -t)
            if total > end:
                total += heapq.heappop(pq)
        return len(pq)

# Author: RT
# Date: 2023-02-23T13:27:24.682Z
# URL: https://leetcode.com/problems/ipo/


import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = sorted(zip(capital, profits))
        n = len(projects)
        choices = []  # use as max-heap
        p = 0
        for _ in range(k):
            while p < n and projects[p][0] <= w:
                heapq.heappush(choices, -projects[p][1])
                p += 1

            if not choices:
                break

            w += -heapq.heappop(choices)

        return w

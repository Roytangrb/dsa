# Author: RT
# Date: 2023-05-23T05:43:16.340Z
# URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/


import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.h = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heapreplace(self.h, val)

        return self.h[0]

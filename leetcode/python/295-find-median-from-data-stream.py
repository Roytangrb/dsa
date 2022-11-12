# Author: RT
# Date: 2022-11-12T04:01:28.126Z
# URL: https://leetcode.com/problems/find-median-from-data-stream/


import heapq


class MedianFinder:
    def __init__(self):
        self.front = []  # max heap
        self.rear = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.front, -num)
        # maintain partitioning: all(front) < all(rear)
        heapq.heappush(self.rear, -heapq.heappop(self.front))
        # maintain size:
        if len(self.rear) > len(self.front):
            heapq.heappush(self.front, -heapq.heappop(self.rear))

    def findMedian(self) -> float:
        if len(self.front) == len(self.rear):
            return (self.rear[0] - self.front[0]) / 2
        else:
            return -self.front[0]

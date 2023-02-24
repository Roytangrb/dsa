# Author: RT
# Date: 2023-02-24T16:01:44.252Z
# URL: https://leetcode.com/problems/minimize-deviation-in-array/


import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        minimum = float("inf")
        max_heap = []

        for num in nums:
            to_max = num * 2 if num & 1 else num
            max_heap.append(-to_max)
            minimum = min(minimum, to_max)

        heapq.heapify(max_heap)

        ans = float("inf")
        while True:
            top = -heapq.heappop(max_heap)
            ans = min(ans, top - minimum)
            if top & 1:
                # the smallest possible maximum value after
                # all divide operation
                break
            else:
                # maintain minimum value after every divide
                minimum = min(minimum, top // 2)
                heapq.heappush(max_heap, -(top // 2))

        return ans

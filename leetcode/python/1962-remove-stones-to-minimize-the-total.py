# Author: RT
# Date: 2022-12-28T06:16:04.345Z
# URL: https://leetcode.com/problems/remove-stones-to-minimize-the-total/


import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            pile = -heapq.heappop(piles)
            heapq.heappush(piles, pile // 2 - pile)

        return -sum(piles)

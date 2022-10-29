# Author: RT
# Date: 2022-10-29T06:18:03.478Z
# URL: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

import heapq


class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        growq = [(-gt, i) for i, gt in enumerate(growTime)]
        heapq.heapify(growq)

        curr = 0
        et = 0
        while growq:
            to_plant = heapq.heappop(growq)
            gt, i = -to_plant[0], to_plant[1]
            pt = plantTime[i]

            curr += pt
            et = max(et, curr + gt)

        return et

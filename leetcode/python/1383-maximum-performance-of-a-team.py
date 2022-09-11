# Author: RT
# Date: 2022-09-11T09:38:08.391Z
# URL: https://leetcode.com/problems/maximum-performance-of-a-team/


import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        M = 1_000_000_007
        engs = sorted(zip(efficiency, speed), key=lambda d: d[0], reverse=True)

        selected = []  # k fastest speed with current running minimal efficiency
        speed_sum = ans = 0
        for eff, spd in engs:
            if len(selected) == k:
                speed_sum -= heapq.heappop(selected)

            heapq.heappush(selected, spd)
            speed_sum += spd
            ans = max(ans, speed_sum * eff)

        return ans % M

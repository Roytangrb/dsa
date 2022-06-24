# Author: RT
# Date: 2022-06-24T15:37:14.246Z
# URL: https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        # curr_max_original + sum(others) = curr_max

        if len(target) == 1:
            return target == [1]

        total = 0
        items = []
        for v in target:
            total += v
            items.append(-v)

        heapq.heapify(items)
        while -items[0] > 1:
            v = -items[0]

            sum_others = total - v
            if sum_others == 1:  # Edge case division by 1 when n=2
                return True

            # prev_v = v - sum_others
            prev_v = v % sum_others  # optimization
            total -= v - prev_v

            if prev_v < 1 or prev_v == v:
                return False

            heapq.heapreplace(items, -prev_v)

        return True

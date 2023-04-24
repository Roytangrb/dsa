# Author: RT
# Date: 2023-04-24T04:18:50.567Z
# URL: https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        for w in stones:
            buckets[w] += 1

        biggest = 0
        curr = max_weight
        while curr > 0:
            if not buckets[curr]:
                curr -= 1
            elif not biggest:
                buckets[curr] %= 2
                if buckets[curr]:
                    biggest = curr
                curr -= 1
            else:
                buckets[curr] -= 1
                if biggest - curr <= curr:
                    buckets[biggest - curr] += 1
                    biggest = 0
                else:
                    biggest -= curr

        return biggest

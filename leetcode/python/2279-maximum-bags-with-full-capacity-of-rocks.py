# Author: RT
# Date: 2022-12-27T10:02:48.049Z
# URL: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/


from bisect import bisect_right
from itertools import accumulate


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        return bisect_right(
            list(accumulate(sorted(c - r for c, r in zip(capacity, rocks)))),
            additionalRocks,
        )

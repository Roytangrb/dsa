# Author: RT
# Date: 2023-07-08T03:39:23.522Z
# URL: https://leetcode.com/problems/put-marbles-in-bags/description/


from itertools import pairwise


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0

        # we need to insert at k - 1 interval to make k groups
        # the left and right numbers surrounding the interval
        # should be added to the score.
        # max score = k - 1 largest sum of pair
        # min score = k - 1 smallest sum of pair
        # perf: the pairs do not need to be fully sorted, could
        # use quick select to sum the largest/smallest k - 1 pairs
        pair_sums = sorted((a + b for a, b in pairwise(weights)))
        # add ith largest and subtract ith smallest
        return sum((pair_sums[-i - 1] - pair_sums[i] for i in range(k - 1)))

# Author: RT
# Date: 2022-12-25T06:34:51.683Z
# URL: https://leetcode.com/problems/longest-subsequence-with-limited-sum/


from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        seq_sums = list(accumulate(sorted(nums)))
        return [bisect_right(seq_sums, q) for q in queries]

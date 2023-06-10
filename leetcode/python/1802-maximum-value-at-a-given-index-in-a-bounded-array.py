# Author: RT
# Date: 2023-06-10T18:32:42.779Z
# URL: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
import bisect


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # make [:index] increasing and [index:] decreasing
        # such that sum of nums <= maxSum, i.e. maximize sum in the
        # prefix and minimize sum in the suffix
        class Nums:
            def __getitem__(self, x):
                """Return sum of nums when the x is chosen for nums[index]"""
                first = x - index
                last = x - (n - index - 1)
                s = (first + x - 1) * index // 2 + (x + last) * (n - index) // 2
                # clamp prefix and suffix to 1s
                if first <= 0:
                    s += (1 - first) * (1 - first + 1) // 2
                if last <= 0:
                    s += (1 - last) * (1 - last + 1) // 2

                return s

        x = bisect.bisect_right(Nums(), maxSum, lo=1, hi=maxSum // n + n + 1)
        return x - 1

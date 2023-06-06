# Author: RT
# Date: 2023-06-06T03:46:01.210Z
# URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)
        first, last = min(arr), max(arr)
        p, q = divmod(last - first, n - 1)
        if q:
            return False
        if p == 0:
            return True

        nums = set(arr)

        for _ in range(n):
            if first not in nums:
                return False

            first += p

        return True

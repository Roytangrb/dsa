# Author: RT
# Date: 2023-07-04T23:38:08.421Z
# URL: https://leetcode.com/problems/single-number-ii/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Intuition: first and second are 2 sets of bits to record how many times
        # we encounter each bit. Each number could appear 3 times at most, there
        # are 3 states for each bit, thus we need 3 bit (2 sets) to encode the information.
        # For each bit:
        # on 1st encounter, bit is set on first (0 -> 1)
        # on 2nd encounter, bit is unset on first (1 -> 0), and set on second (0 -> 1)
        # on 3rd encounter, bit is not set on first (0 -> 0), and unset on second (1 -> 0)
        # Therefore, the bits of single number will remain set on first after processing.
        first = second = 0
        for num in nums:
            first = (first ^ num) & ~second
            second = (second ^ num) & ~first

        return first

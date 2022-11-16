# Author: RT
# Date: 2022-11-16T15:40:56.090Z
# URL: https://leetcode.com/problems/guess-number-higher-or-lower/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                l = mid + 1
            else:
                r = mid - 1

        return 0

# Author: RT
# Date: 2022-11-06T08:54:13.615Z
# URL: https://leetcode.com/problems/orderly-queue/


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # When k == 1:
        #   the string can only be "rotated", append first char to the end
        # When k > 1:
        #   say k == 2, we can swap first and second char by appending second
        #   char to the end, and then rotate. Given enough moves, we can swap
        #   any pairs, thus all permutation is possible.
        if k == 1:
            start = min(range(len(s)), key=lambda i: s[i:] + s[:i])
            return s[start:] + s[:start]

        return "".join(sorted(list(s)))

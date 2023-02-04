# Author: RT
# Date: 2023-02-04T10:16:51.075Z
# URL: https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        R = numRows
        if R == 1:
            return s

        cs = []
        for i, c in enumerate(s):
            # calc row, col in zig-zag repr
            j = i % (2 * R - 2)
            row = j if j < R else R - 1 - (j + 1 - R)
            k = i // (2 * R - 2)
            col = k * (R - 1) + max(j - R + 1, 0)
            # record char by zig-zag pos
            cs.append((row, col, c))

        return "".join(x[2] for x in sorted(cs))


# TODO: O(n) solution with original string traversal by jump pattern

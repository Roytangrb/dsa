# Author: RT
# Date: 2023-09-29T03:04:04.409Z
# URL: https://leetcode.com/problems/optimal-partition-of-string/


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        seen = 0
        for c in s:
            flag = 1 << (ord(c) - ord("a"))
            if flag & seen:
                ans += 1
                seen = 0  # reset

            seen |= flag

        if seen:
            ans += 1

        return ans

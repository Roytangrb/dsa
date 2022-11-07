# Author: RT
# Date: 2022-11-07T14:47:27.105Z
# URL: https://leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, num: int) -> int:
        return num + next(
            (
                3 * 10 ** (len(str(num)) - i - 1)
                for i, s in enumerate(str(num))
                if s == "6"
            ),
            0,
        )

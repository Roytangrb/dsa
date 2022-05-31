# Author: RT
# Date: 2022-05-31T15:28:16.720Z
# URL: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        value = int(s[:k], 2)
        seen = {value}
        ones = (1 << k) - 1  # for unsetting leftmost bit
        count = 2**k - 1  # count of binary code of length k - initial value

        for i in range(k, n):
            # unset leftmost bit and left-shift
            value <<= 1
            value &= ones

            # set rightmost bit
            value |= int(s[i])

            if value not in seen:
                seen.add(value)
                count -= 1

                if not count:
                    return True

        return False

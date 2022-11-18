# Author: RT
# Date: 2022-11-18T14:19:59.963Z
# URL: https://leetcode.com/problems/ugly-number/


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n & 1 == 0:
                n >>= 1
            elif n % 5 == 0:
                n //= 5
            elif n % 3 == 0:
                n //= 3
            else:
                return False

        return True

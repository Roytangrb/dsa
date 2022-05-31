# Author: RT
# Date: 2022-05-31T15:59:19.154Z
# URL: https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s1 = 1 if dividend >= 0 else 0
        s2 = 1 if divisor > 0 else 0
        sign = s1 ^ s2
        MIN = -(2**31)
        MAX = 2**31 - 1

        if not s1:
            dividend = -dividend
        if not s2:
            divisor = -divisor

        if divisor == 1:
            return max(min(-dividend if sign else dividend, MAX), MIN)

        # used multiplication, not allowed
        # ans = self.long_division_base10(dividend, divisor)
        ans = self.long_division_base2(dividend, divisor)

        return max(min(-ans if sign else ans, MAX), MIN)

    def long_division_base10(self, a: int, b: int):
        ans = ""
        a_str = str(a)
        i = remainder = 0
        while i < len(a_str):
            remainder *= 10
            remainder += int(a_str[i])
            digit = 0
            while remainder >= b:
                remainder -= b
                digit += 1
            ans += str(digit)
            i += 1

        return int(ans)

    def long_division_base2(self, a: int, b: int):
        ans = 0
        mask = self.gbp(a)
        remainder = 0
        while mask:
            remainder <<= 1
            remainder |= 1 if (a & mask) else 0

            ans <<= 1
            if remainder >= b:
                remainder -= b
                ans |= 1

            mask >>= 1

        return ans

    def gbp(self, n: int):
        """Greatest bit position"""
        # fill all bits to 1 to the right of gbp
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        # flip all 1-bits
        n += 1

        # original gbp
        return n >> 1

# Author: RT
# Date: 2023-02-01T12:27:05.650Z
# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/


from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if str1 + str2 != str2 + str1:
            return ""

        return str1[: gcd(m, n)]

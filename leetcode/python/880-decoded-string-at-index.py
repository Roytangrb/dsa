# Author: RT
# Date: 2023-09-27T22:30:42.736Z
# URL: https://leetcode.com/problems/decoded-string-at-index/


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """O(n) where n = len(s)"""
        decoded_length = 0
        for i, c in enumerate(s):
            decoded_length += decoded_length * (int(c) - 1) if c.isdigit() else 1
            if decoded_length >= k:
                break

        for j in reversed(range(i + 1)):
            c = s[j]
            if c.isdigit():
                decoded_length //= int(c)
                k %= decoded_length
                # the kth (1 based) char of a string with a repeating word w
                # is the equal to w[k % len(w)]
                # e.g. abc|abc|abc with w = abc, 1st char == 4th chat == 7th char
            else:
                if decoded_length == k or k == 0:
                    return c
                decoded_length -= 1

        assert False, "never"


class Solution_TLE:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """O(k) time, O(1) space given len(s) <= 100"""

        def gen(i):
            if i == 0:
                yield s[0]
            else:
                if ord("2") <= ord(s[i]) <= ord("9"):
                    for _ in range(int(s[i])):
                        yield from gen(i - 1)
                else:
                    yield from gen(i - 1)
                    yield s[i]

        g = gen(len(s) - 1)
        for _ in range(k - 1):
            next(g)

        return next(g)

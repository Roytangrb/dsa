# Author: RT
# Date: 2022-10-25T13:06:48.318Z
# URL: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


from itertools import zip_longest


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        g1 = (c for w in word1 for c in w)
        g2 = (c for w in word2 for c in w)

        return all(a == b for a, b in zip_longest(g1, g2))

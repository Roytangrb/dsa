# Author: RT
# Date: 2022-05-29T16:08:59.396Z
# URL: https://leetcode.com/problems/maximum-product-of-word-lengths/

from collections import Counter


class Solution:
    def maxProduct(self, words: list[str]) -> int:
        bitsets = Counter()
        for word in words:
            bitset = 0
            for c in word:
                mask = 1 << (ord("z") - ord(c))
                bitset |= mask
            bitsets[bitset] = max(bitsets[bitset], len(word))

        length_sorted = bitsets.most_common()
        n = len(length_sorted)
        ans = 0
        for i in range(n):
            si, li = length_sorted[i]
            for j in range(i + 1, n):
                sj, lj = length_sorted[j]
                if not (si & sj):
                    ans = max(ans, li * lj)
                    break

        return ans

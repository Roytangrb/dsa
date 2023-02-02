# Author: RT
# Date: 2023-02-02T13:26:54.639Z
# URL: https://leetcode.com/problems/verifying-an-alien-dictionary/


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_mp = {c: i for i, c in enumerate(order)}

        def compare(a: str, b: str):
            m, n = len(a), len(b)
            for i in range(min(m, n)):
                va = order_mp[a[i]]
                vb = order_mp[b[i]]

                if va < vb:
                    return -1
                elif va > vb:
                    return 1

            if len(a) == len(b):
                return 0
            elif len(a) < len(b):
                return -1
            else:
                return 1

        return all(compare(words[i - 1], words[i]) <= 0 for i in range(1, len(words)))

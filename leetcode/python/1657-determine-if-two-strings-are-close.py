# Author: RT
# Date: 2022-12-02T14:24:53.085Z
# URL: https://leetcode.com/problems/determine-if-two-strings-are-close/


from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(
            c2.values()
        )

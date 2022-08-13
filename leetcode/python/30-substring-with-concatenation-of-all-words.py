# Author: RT
# Date: 2022-08-13T15:59:18.499Z
# URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/


from collections import Counter
from functools import cache


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n, m = len(words), len(words[0])
        t = self.build_trie(words)
        self.t = t
        self.s = s

        ans = []
        for start in range(len(s)):
            # sliding window
            l, r = start, start + m
            seen = Counter()  # count of seen words
            used = 0
            while count := self.is_in_words(l, r):
                word = s[l:r]
                if seen[word] >= count:
                    break

                seen[word] += 1
                used += 1

                if used == n:
                    ans.append(start)
                    break

                l = r
                r += m

        return ans

    @cache
    def is_in_words(self, l: int, r: int) -> int:
        """Return count of found word"""
        if r > len(self.s):
            return 0

        _t = self.t
        for i in range(l, r):
            if self.s[i] not in _t:
                return 0
            _t = _t[self.s[i]]

        return _t["count"]

    def build_trie(self, words: list[str]) -> dict:
        t = {}
        for i, word in enumerate(words):
            _t = t
            for c in word:
                if c not in _t:
                    _t[c] = {}
                _t = _t[c]
            _t["count"] = _t.get("count", 0) + 1

        return t

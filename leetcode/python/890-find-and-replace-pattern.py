# Author: RT
# Date: 2022-07-29T16:05:08.616Z
# URL: https://leetcode.com/problems/find-and-replace-pattern/


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        id_iter = iter(range(26))
        char_idx = {}
        pattern_idx = []
        for c in pattern:
            if c not in char_idx:
                char_idx[c] = next(id_iter)

            pattern_idx.append(char_idx[c])

        ans = []
        for word in words:
            id_iter = iter(range(26))
            char_idx = {}
            for c, idx in zip(word, pattern_idx):
                if c not in char_idx:
                    char_idx[c] = next(id_iter)
                if char_idx[c] != idx:
                    break
            else:
                ans.append(word)

        return ans

    def findAndReplacePattern_bijection_maps(
        self, words: list[str], pattern: str
    ) -> list[str]:
        """Use two maps to verify the bijection"""

        def match(word: str):
            forward, backward = {}, {}
            for w, p in zip(word, pattern):
                if w not in forward:
                    forward[w] = p
                if p not in backward:
                    backward[p] = w
                if (forward[w], backward[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words))

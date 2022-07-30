# Author: RT
# Date: 2022-07-30T06:25:06.067Z
# URL: https://leetcode.com/problems/word-subsets/


from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """Reduce word list 2 to a single word"""
        counters = {w: Counter(w) for w in words1}
        target = Counter()
        for w in words2:
            for c, freq in Counter(w).items():
                target[c] = max(target[c], freq)

        return [
            w
            for w in words1
            if all(freq <= counters[w][c] for c, freq in target.items())
        ]

    def brute_force(self, words1: list[str], words2: list[str]) -> list[str]:
        counters = {w: Counter(w) for w in words1}

        return [
            w1
            for w1, cs in counters.items()
            if all(
                all(freq <= cs[c] for c, freq in Counter(w2).items()) for w2 in words2
            )
        ]

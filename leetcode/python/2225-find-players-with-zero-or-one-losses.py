# Author: RT
# Date: 2022-11-28T14:38:34.880Z
# URL: https://leetcode.com/problems/find-players-with-zero-or-one-losses/


from collections import Counter


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        W = set()
        L = Counter()
        for winner, loser in matches:
            W.add(winner)
            L[loser] += 1

        return [
            sorted([p for p in W if p not in L]),
            sorted([p for p, c in L.items() if c == 1]),
        ]

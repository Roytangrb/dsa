# Author: RT
# Date: 2022-07-12T16:22:14.773Z
# URL: https://leetcode.com/problems/matchsticks-to-square/

from itertools import permutations


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """A bin packing issue"""
        matchsticks.sort(reverse=True)

        n = len(matchsticks)
        if n < 4:
            return False
        total = sum(matchsticks)
        a, remain = divmod(total, 4)
        if remain or matchsticks[0] > a:
            return False

        sides = [a] * 4
        memo = set()

        def backtrack(i):
            if i == n:
                return not sum(sides)

            key = tuple(sides)
            if key in memo:
                return False

            for j in range(4):
                sides[j] -= matchsticks[i]
                if sides[j] >= 0 and backtrack(i + 1):
                    return True
                sides[j] += matchsticks[i]

            # order of sides do no matter, prune tree if combination cannot form square
            for impossible_key in permutations(key):
                memo.add(impossible_key)

            return False

        return backtrack(0)

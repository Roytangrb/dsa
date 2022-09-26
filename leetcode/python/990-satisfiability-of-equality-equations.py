# Author: RT
# Date: 2022-09-26T14:26:34.228Z
# URL: https://leetcode.com/problems/satisfiability-of-equality-equations/


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        idx = lambda c: ord("z") - ord(c)
        parse = lambda e: (idx(e[0]), idx(e[-1]), e[1] == "=")

        parents = list(range(26))
        rank = [1] * 26

        for e in equations:
            x, y, is_equal = parse(e)
            if is_equal:
                self.union(parents, rank, x, y)

        for e in equations:
            x, y, is_equal = parse(e)
            if not is_equal and self.find(parents, x) == self.find(parents, y):
                return False

        return True

    def find(self, parents: list[int], x: int) -> int:
        if parents[x] != x:
            parents[x] = self.find(parents, parents[x])
        return parents[x]

    def union(self, parents: list[int], rank: list[int], x: int, y: int):
        px = self.find(parents, x)
        py = self.find(parents, y)

        if px == py:
            return

        rx, ry = rank[px], rank[py]
        if rx < ry:
            parents[px] = py
        elif rx > ry:
            parents[py] = px
        else:
            parents[py] = px
            rank[px] += 1

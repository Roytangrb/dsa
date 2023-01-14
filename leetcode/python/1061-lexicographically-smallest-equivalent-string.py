# Author: RT
# Date: 2023-01-14T17:24:15.295Z
# URL: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = list(range(26))

        for a, b in zip(s1, s2):
            self.union(ord(a) - ord("a"), ord(b) - ord("a"), parents)

        return "".join(
            chr(ord("a") + self.find(ord(c) - ord("a"), parents)) for c in baseStr
        )

    def find(self, x: int, parents: list[int]) -> int:
        if parents[x] != x:
            parents[x] = self.find(parents[x], parents)

        return parents[x]

    def union(self, x: int, y: int, parents: list[int]):
        px = self.find(x, parents)
        py = self.find(y, parents)
        if px == py:
            return

        px, py = min(px, py), max(px, py)
        parents[py] = px

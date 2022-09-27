# Author: RT
# Date: 2022-09-27T13:29:18.061Z
# URL: https://leetcode.com/problems/push-dominoes/


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n

        f = 0
        for i in range(n):
            curr = dominoes[i]
            if curr == "R":
                f = n
            elif curr == "L":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        f = 0
        for i in range(n - 1, -1, -1):
            curr = dominoes[i]
            if curr == "R":
                f = 0
            elif curr == "L":
                f = n
            else:
                f = max(f - 1, 0)
            force[i] -= f

        return "".join("." if f == 0 else "R" if f > 0 else "L" for f in force)

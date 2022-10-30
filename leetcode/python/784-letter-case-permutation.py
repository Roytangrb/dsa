# Author: RT
# Date: 2022-10-30T06:22:45.596Z
# URL: https://leetcode.com/problems/letter-case-permutation/


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        n = len(s)
        ans = []
        cs = list(s)

        def backtrack(i: int):
            if i == n:
                ans.append("".join(cs))
                return

            backtrack(i + 1)
            if not cs[i].isdigit():
                c = cs[i]
                cs[i] = c.lower() if c.isupper() else c.upper()
                backtrack(i + 1)
                cs[i] = c

        backtrack(0)

        return ans

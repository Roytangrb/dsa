# Author: RT
# Date: 2022-09-03T14:13:53.482Z
# URL: https://leetcode.com/problems/numbers-with-same-consecutive-differences/


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        ans = []

        def backtrack(i: int, prev: int, num: int):
            if i == n:
                ans.append(num)
                return

            if (curr := prev - k) >= 0:
                backtrack(i + 1, curr, num * 10 + curr)
            if k and (curr := prev + k) <= 9:
                backtrack(i + 1, curr, num * 10 + curr)

        for d in range(1, 10):
            backtrack(1, d, d)

        return ans

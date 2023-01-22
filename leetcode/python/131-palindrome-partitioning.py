# Author: RT
# Date: 2023-01-22T16:17:40.763Z
# URL: https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(i: int, prev: int, subs: list[str]):
            if i == n:
                if subs and prev == n:
                    ans.append(list(subs))

                return

            backtrack(i + 1, prev, subs)
            if is_palindrome(prev, i):
                subs.append(s[prev : i + 1])
                backtrack(i + 1, i + 1, subs)
                subs.pop()

        backtrack(0, 0, [])
        return ans

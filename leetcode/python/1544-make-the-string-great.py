# Author: RT
# Date: 2022-11-08T14:30:27.375Z
# URL: https://leetcode.com/problems/make-the-string-great/


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

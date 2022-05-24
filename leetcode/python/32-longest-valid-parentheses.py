# Author: RT
# Date: 2022-05-24T16:31:40.737Z
# URL: https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        left = -1

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif stack:  # there is a valid substr ending at i
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    ans = max(ans, i - left)
            else:  # more close brackets than open brackets in (left, i]
                left = i

        return ans

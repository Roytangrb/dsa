# Author: RT
# Date: 2022-12-17T12:41:36.507Z
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/


from operator import add, mul, sub


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def div(a, b):
            return int(a / b)

        op_map = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
        }
        stack = []
        for token in tokens:
            if token in op_map:
                b = stack.pop()
                a = stack.pop()
                stack.append(op_map[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()

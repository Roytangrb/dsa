# Author: RT
# Date: 2022-11-20T09:26:47.416Z
# URL: https://leetcode.com/problems/basic-calculator/


from collections import deque
from itertools import chain
from typing import Iterable, Iterator, Literal, NamedTuple


class Token(NamedTuple):
    lexeme: str
    token_type: Literal["operand", "operator", "paren"]


class Solution:
    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        stack = []
        for token, _ in tokens:
            if token == ")":
                expr = deque()
                while stack[-1] != "(":
                    expr.appendleft(stack.pop())
                stack.pop()
                stack.append(self.eval_expr(expr))
            else:
                stack.append(token)

        return self.eval_expr(stack)

    def eval_expr(self, ops: Iterable[str]) -> int:
        ret = 0
        sign = 1
        for op in ops:
            if op == "+":
                sign = 1
            elif op == "-":
                sign = -1
            else:
                ret += int(op) * sign

        return ret

    def tokenize(self, s: str) -> Iterator[Token]:
        lexeme = ""
        for c in chain(s, "$"):
            if c == " ":
                continue
            if not lexeme:
                lexeme = c
                continue
            if lexeme.isnumeric() and c.isdigit():
                lexeme += c
                continue
            if lexeme.isnumeric():
                yield Token(lexeme, "operand")
            elif lexeme in ("+", "-"):
                yield Token(lexeme, "operator")
            elif lexeme in ("(", ")"):
                yield Token(lexeme, "paren")
            else:
                assert False, f"Unknown character {c=}"

            lexeme = c

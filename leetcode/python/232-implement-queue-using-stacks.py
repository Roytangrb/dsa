# Author: RT
# Date: 2022-12-16T15:49:08.183Z
# URL: https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        self.peeked = -1
        self.s1 = []  # first enqueued at the bottom
        self.s2 = []  # first enqueued on the top

    def push(self, x: int) -> None:
        if self.empty():
            self.peeked = x

        while self.s2:
            self.s1.append(self.s2.pop())

        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())

        v = self.s2.pop()
        self.peeked = self.s2[-1] if self.s2 else -1

        return v

    def peek(self) -> int:
        return self.peeked

    def empty(self) -> bool:
        return not (self.s1 or self.s2)

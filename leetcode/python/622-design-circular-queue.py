# Author: RT
# Date: 2022-09-25T06:39:18.160Z
# URL: https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue:
    """Non-thread-safe implementation"""

    size: int = 0
    capacity: int = 0
    head: int | None = None
    values: list[int]

    def __init__(self, k: int):
        self.values = [0] * k
        self.capacity = k

    @property
    def rear(self):
        return (self.head + self.size - 1) % self.capacity

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.head is None:
            self.head = 0

        self.size += 1
        self.values[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.values[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.values[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Author: RT
# Date: 2022-11-09T11:39:52.618Z
# URL: https://leetcode.com/problems/online-stock-span/


class StockSpanner:
    def __init__(self):
        self.day = 0
        self.stack = []

    def next(self, price: int) -> int:
        self.day += 1
        prev = 0
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        prev = self.stack[-1][1] if self.stack else 0
        self.stack.append((price, self.day))

        return self.day - prev

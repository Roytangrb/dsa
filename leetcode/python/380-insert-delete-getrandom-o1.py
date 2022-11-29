# Author: RT
# Date: 2022-11-29T13:29:31.495Z
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1/


import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.next_i = 0
        self.index = {}

    def insert(self, val: int) -> bool:
        if val not in self.index:
            if self.next_i < len(self.arr):
                self.arr[self.next_i] = val
            else:
                self.arr.append(val)
            self.index[val] = self.next_i
            self.next_i += 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.index:
            last = self.arr[self.next_i - 1]
            i = self.index[val]
            self.arr[i] = last
            self.index[last] = i
            self.next_i -= 1
            del self.index[val]
            return True

        return False

    def getRandom(self) -> int:
        i = random.randint(0, self.next_i - 1)
        return self.arr[i]

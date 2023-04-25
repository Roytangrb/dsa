# Author: RT
# Date: 2023-04-25T01:59:17.855Z
# URL: https://leetcode.com/problems/smallest-number-in-infinite-set/


from sortedcontainers import SortedSet


class SmallestInfiniteSet:
    _added_back: SortedSet
    _i: int  # numbers in [i, right bound + 1] are included

    def __init__(self):
        self._added_back = SortedSet()
        self._i = 1

    def popSmallest(self) -> int:
        if not self._added_back:
            ret = self._i
            self._i += 1
            return ret

        return self._added_back.pop(0)

    def addBack(self, num: int) -> None:
        if num >= self._i:
            return

        self._added_back.add(num)

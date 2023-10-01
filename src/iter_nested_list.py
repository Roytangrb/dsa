"""Iterate nested list with generator

https://leetcode.com/problems/flatten-nested-list-iterator/
"""

from data_structures.nested_list import NestedInteger


class NestedIterator:
    def __init__(self, nested_list: list[NestedInteger]):
        self.peeked = None
        self.gen = self.generate(nested_list)

    def generate(self, nested_list: list[NestedInteger]):
        for el in nested_list:
            if el.is_integer():
                yield el.get_integer()
            else:
                yield from self.generate(el.get_list())

    def next(self) -> int:
        """Return peeked value"""
        return self.peeked

    def hasNext(self) -> bool:
        """Peek and advance the generator"""
        self.peeked = next(self.gen, None)
        return self.peeked is not None


if __name__ == "__main__":
    testcases = (
        ([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1]),
        ([1, [4, [6]]], [1, 4, 6]),
        ([1], [1]),
    )

    for nested_list, expected in testcases:
        it = NestedIterator([NestedInteger.from_list(nested_list)])
        actual = []
        while it.hasNext():
            actual.append(it.next())

        assert actual == expected

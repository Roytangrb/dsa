"""Utility data types or data structures for binary trees"""

import sys
from typing import Optional, TextIO


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

    def height(self) -> int:
        h = 0
        if self.left:
            h = 1 + self.left.height()
        if self.right:
            h = max(h, 1 + self.right.height())

        return h

    @classmethod
    def from_values(cls: type["TreeNode"], values: list[Optional[int]]) -> "TreeNode":
        """Construct binary tree with values from root to last level, left to right"""
        if not values:
            raise ValueError("Empty values, use None as root instead.")
        if values[0] is None:
            raise ValueError("Root cannot be None.")

        root = cls(values[0])
        level = [root]
        i, n = 1, len(values)
        while level:
            next_level = []
            for parent in level:
                for k in (0, 1):
                    # trailing null leave nodes could be omitted in the last level
                    val = values[i + k] if i + k < n else None
                    if val is not None:
                        child = cls(val)
                        if not k:
                            parent.left = child
                        else:
                            parent.right = child
                        next_level.append(child)
                # take two values as children for a non-null parent
                i += 2

            level = next_level

        return root

    def visualize(self, out: Optional[TextIO] = sys.stdout):
        """Pretty print binary tree, default to stdout"""
        level = [self]

        while level:
            print(*level, sep=" ", file=out)
            next_level = []

            for node in level:
                if node:
                    next_level.extend([node.left, node.right])

            level = next_level

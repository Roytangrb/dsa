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

    @classmethod
    def from_values(cls: type["TreeNode"], values: list[Optional[int]]) -> "TreeNode":
        """Construct binary tree with values from root to last layer, left to right"""
        if not values:
            raise ValueError("Empty values, use None as root instead.")
        if values[0] is None:
            raise ValueError("Root cannot be None.")

        root = cls(values[0])
        layer = [root]
        i, depth, n = 1, 1, len(values)
        while i < n:
            next_layer = []
            for j in range(i, min(n, i + 2**depth)):
                value = values[j]
                if value is not None:
                    next_layer.append(cls(value))
                else:
                    next_layer.append(None)

            for k, child in enumerate(next_layer):
                parent, is_right = divmod(k, 2)
                if is_right:
                    layer[parent].right = child
                else:
                    layer[parent].left = child

            i += len(next_layer)
            depth += 1
            layer = next_layer

        return root

    def visualize(self, out: Optional[TextIO] = sys.stdout):
        """Pretty print binary tree, default to stdout"""
        layer = [self]

        while layer:
            print(*layer, sep=" ", file=out)
            next_layer = []

            for node in layer:
                if node:
                    next_layer.extend([node.left, node.right])

            layer = next_layer

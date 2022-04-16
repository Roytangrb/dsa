"""Utility data types or data structures for binary trees"""

from typing import Optional


class TreeNode:
    val: Optional[int]
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: Optional[int] = None,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_values(
        cls: type["TreeNode"], values: list[Optional[int]]
    ) -> Optional["TreeNode"]:
        """Construct binary tree with values from root to last layer, left to right"""
        if not values:
            return None

        root = cls(values[0])
        layer = [root]
        i, depth, n = 1, 1, len(values)
        while i < n:
            next_layer = [cls(values[j]) for j in range(i, min(n, i + 2**depth))]
            for k, child in enumerate(next_layer):
                parent, is_left = divmod(k, 2)
                if is_left:
                    layer[parent].left = child
                else:
                    layer[parent].right = child

            i += len(next_layer)
            depth += 1
            layer = next_layer

        return root

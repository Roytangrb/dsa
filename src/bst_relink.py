"""Re-arrange nodes in BST to increasing order search tree

https://leetcode.com/problems/increasing-order-search-tree/
"""

from typing import Optional

import bst_iterator
from data_structures.binary_tree import TreeNode


def relink_bst_to_increasing(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Use dummy sentinel node to handle root of the re-linked result list
    ans = prev = TreeNode(0)

    def inorder(node: Optional[TreeNode]):
        nonlocal prev

        if not node:
            return

        inorder(node.left)

        node.left = None
        prev.right = node
        prev = node

        inorder(node.right)

    inorder(root)

    return ans.right


if __name__ == "__main__":
    testcases = (
        TreeNode.from_values([5, 1, 7]),
        TreeNode.from_values([2, 1, 4, None, None, 3]),
        TreeNode.from_values([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]),
    )

    for root in testcases:
        expected = list(bst_iterator.iter_inorder(root))
        root = relink_bst_to_increasing(root)
        actual = []
        while root:
            actual.append(root)
            root = root.right

        assert (
            actual == expected
        ), f"BST is not transformed to increasing list, {expected=}, {actual=}."

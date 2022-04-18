"""Reverse In-order traversal with Morris Traversal

https://leetcode.com/problems/convert-bst-to-greater-tree/
Update node values to the in-order suffix sum
"""

from typing import Optional

import bst_iterator
from data_structures.binary_tree import TreeNode


def get_successor(node: TreeNode) -> TreeNode:
    """Return successor for link/unlink from it to the current node"""
    succ = node.right
    assert succ, "get_successor should be called when node has right sub-tree."

    while succ.left is not None and succ.left is not node:
        succ = succ.left

    return succ


def convert_bst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    suffix = 0
    curr = root
    while curr is not None:
        if curr.right is None:
            suffix += curr.val
            curr.val = suffix
            curr = curr.left
        else:
            succ = get_successor(curr)
            # the successor's left child is originally null by definition
            if succ.left is None:
                # link successor to the current node
                succ.left = curr
                curr = curr.right
            else:
                # right sub-tree visited, returning to the current node, unlink
                # the successor's link to current node created in previous pass
                succ.left = None
                suffix += curr.val
                curr.val = suffix
                curr = curr.left

    return root


if __name__ == "__main__":
    testcases = (
        (
            TreeNode.from_values(
                [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
            ),
            TreeNode.from_values(
                [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
            ),
        ),
        (
            TreeNode.from_values([0, None, 1]),
            TreeNode.from_values([1, None, 1]),
        ),
    )
    for root, converted in testcases:
        actual = [d.val for d in bst_iterator.iter_inorder(convert_bst(root))]
        expected = [d.val for d in bst_iterator.iter_inorder(converted)]

        assert actual == expected

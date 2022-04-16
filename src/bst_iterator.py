"""Traverse binary search tree without recursion"""

from typing import Iterator, Optional

from data_structures.binary_tree import TreeNode


def iter_inorder(root: Optional[TreeNode]) -> Iterator[TreeNode]:
    stack: list[TreeNode] = []
    curr: Optional[TreeNode] = root

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr
            curr = curr.right
        else:
            break


if __name__ == "__main__":
    root = TreeNode.from_values([7, 3, 15, None, None, 9, 20])

    root.visualize()
    print("Inorder:", list(iter_inorder(root)), sep="\n")

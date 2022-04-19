"""Find two swapped elements in a sorted array"""

import bst_iterator
from data_structures.binary_tree import TreeNode


def find_two_swapped(nums: list[int]) -> tuple[int, int]:
    """Return indices of the two swapped elements"""
    n = len(nums)
    x = y = -1
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            y = i

            # first occurrence, nums[i - 1] is the large value swapped to front
            if x == -1:
                x = i - 1
            # second occurrence, nums[i] is the small value swapped to back
            else:
                break

    return x, y


def recover_bst(root: TreeNode):
    """Recover swapped node values in BST

    https://leetcode.com/problems/recover-binary-search-tree/
    """
    x = y = prev = None

    for node in bst_iterator.iter_inorder(root):
        if prev and node.val < prev.val:
            y = node

            if not x:
                x = prev
            else:
                break
        prev = node

    assert x and y
    x.val, y.val = y.val, x.val


# Tests


def test_find_two_swapped():
    testcases = (
        ([2, 1], (0, 1)),
        ([1, 3, 2, 4], (1, 2)),
        ([1, 4, 3, 2, 5], (1, 3)),
    )

    for arr, expected in testcases:
        assert (actual := find_two_swapped(arr)) == expected, f"{expected=}, {actual=}"


def test_recover_bst():
    testcases = (
        (TreeNode.from_values([1, 3, None, None, 2]), [1, 2, 3]),
        (TreeNode.from_values([3, 1, 4, None, None, 2]), [1, 2, 3, 4]),
    )

    for root, expected in testcases:
        recover_bst(root)

        assert (actual := root.inorder()) == expected, f"{expected=}, {actual=}"


if __name__ == "__main__":
    test_find_two_swapped()
    test_recover_bst()

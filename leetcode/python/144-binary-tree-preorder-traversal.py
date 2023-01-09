# Author: RT
# Date: 2023-01-09T13:10:23.612Z
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

from .types import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
            if root
            else []
        )

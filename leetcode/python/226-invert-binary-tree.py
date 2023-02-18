# Author: RT
# Date: 2023-02-18T12:48:07.798Z
# URL: https://leetcode.com/problems/invert-binary-tree/


from .types import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            root.left, root.right = (
                self.invertTree(root.right),
                self.invertTree(root.left),
            )

        return root

# Author: RT
# Date: 2022-07-14T07:19:50.214Z
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import Optional

from .types import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # preorder = [root:left-tree:right-tree]
        # inorder = [left-tree:root:right-tree]
        # use preorder to find current tree
        # use inorder to find left and right trees
        root = TreeNode(preorder[0])
        # linear lookup, worst case O(n**2) time, use hashmap to optimize
        left_size = inorder.index(root.val)

        root.left = self.buildTree(preorder[1 : left_size + 1], inorder[:left_size])
        root.right = self.buildTree(preorder[left_size + 1 :], inorder[left_size + 1 :])

        return root

    def buildTree__optimized(
        self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        # the tree contains unique values
        inorder_idx = {v: i for i, v in enumerate(inorder)}

        def build(l: int, r: int, root_i: int) -> Optional[TreeNode]:
            if l > r:
                return

            root = TreeNode(preorder[root_i])
            j = inorder_idx[root.val]
            left_size = j - l

            root.left = build(l, j - 1, root_i + 1)
            root.right = build(j + 1, r, root_i + left_size + 1)

            return root

        return build(0, len(inorder) - 1, 0)

# Author: RT
# Date: 2022-08-12T17:01:46.091Z
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from .types import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

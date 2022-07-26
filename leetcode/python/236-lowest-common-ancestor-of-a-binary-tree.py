# Author: RT
# Date: 2022-07-26T15:55:04.058Z
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from .types import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        lca = None

        # count p and q seen in subtree, postorder dfs
        # the first node visited with count == 2 is the LCA
        def postorder(node: TreeNode | None) -> int:
            if not node:
                return 0

            count = (
                postorder(node.left) + postorder(node.right) + (node is p or node is q)
            )

            nonlocal lca

            if count == 2 and lca is None:
                lca = node

            return count

        postorder(root)

        return lca

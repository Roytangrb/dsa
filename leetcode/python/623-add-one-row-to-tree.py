# Author: RT
# Date: 2022-10-05T11:59:11.432Z
# URL: https://leetcode.com/problems/add-one-row-to-tree/

from .types import TreeNode


class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        def dfs(node: TreeNode | None, dep: int, parent: TreeNode | None):
            if dep == depth:
                if not parent:
                    return TreeNode(val, node)
                elif node is parent.left:
                    parent.left = TreeNode(val, node)
                    return parent.left
                elif node is parent.right:
                    parent.right = TreeNode(val, None, node)
                    return parent.right
            elif node:
                dfs(node.left, dep + 1, node)
                dfs(node.right, dep + 1, node)

            return node

        return dfs(root, 1, None)

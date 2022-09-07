# Author: RT
# Date: 2022-09-07T12:46:04.596Z
# URL: https://leetcode.com/problems/construct-string-from-binary-tree/


from .types import TreeNode


class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        cs = []

        def dfs(node: TreeNode | None):
            if node:
                cs.append(str(node.val))
                if node.left or node.right:
                    cs.append("(")
                    if node.left:
                        dfs(node.left)
                    cs.append(")")
                if node.right:
                    cs.append("(")
                    dfs(node.right)
                    cs.append(")")

        dfs(root)
        return "".join(cs)

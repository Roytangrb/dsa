# Author: RT
# Date: 2022-12-09T13:23:29.614Z
# URL: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

from .types import TreeNode


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, m: int, s: int) -> int:
            if node:
                val = node.val
                return max(
                    max(abs(m - val), abs(s - val)),
                    dfs(node.left, max(m, val), min(s, val)),
                    dfs(node.right, max(m, val), min(s, val)),
                )

            return 0

        return dfs(root, root.val, root.val)

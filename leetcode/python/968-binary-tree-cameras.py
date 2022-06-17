# Author: RT
# Date: 2022-06-17T15:45:29.829Z
# URL: https://leetcode.com/problems/binary-tree-cameras/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # conceptually children of leave nodes are covered
        covered = {None}

        def dfs(node, p):
            nonlocal ans

            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (
                    (p is None and node not in covered)
                    or (node.left not in covered)
                    or (node.right not in covered)
                ):
                    ans += 1
                    covered.update({p, node, node.left, node.right})

        dfs(root, None)
        return ans

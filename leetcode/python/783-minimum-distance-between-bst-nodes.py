# Author: RT
# Date: 2023-02-17T13:31:09.714Z
# URL: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from .types import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        def inorder(node: TreeNode | None):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        vals = inorder(root)
        prev = next(vals)
        ans = 100_001
        for val in vals:
            ans = min(ans, abs(val - prev))
            prev = val

        return ans

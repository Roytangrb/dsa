# Author: RT
# Date: 2022-12-11T07:19:51.638Z
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

from .types import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = float("-inf")

        def max_gain(node: TreeNode | None):
            """Max gain of path starting at the current node"""
            nonlocal ans
            if node:
                left_gain = max(max_gain(node.left), 0)
                right_gain = max(max_gain(node.right), 0)

                ans = max(ans, left_gain + right_gain + node.val)

                return node.val + max(left_gain, right_gain)

            return 0

        max_gain(root)
        return ans

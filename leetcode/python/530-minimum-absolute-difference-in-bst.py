# Author: RT
# Date: 2023-06-14T01:26:58.513Z
# URL: https://leetcode.com/problems/minimum-absolute-difference-in-bst/


from .types import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        def in_order(node):
            if node:
                yield from in_order(node.left)
                yield node.val
                yield from in_order(node.right)

        ans = float("inf")
        prev = float("inf")
        for num in in_order(root):
            ans = min(ans, abs(num - prev))
            prev = num

        return ans

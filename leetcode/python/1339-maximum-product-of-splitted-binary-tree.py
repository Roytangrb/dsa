# Author: RT
# Date: 2022-12-10T06:02:07.076Z
# URL: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


from .types import TreeNode


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        subtree_sums = set()

        def dfs(node: TreeNode | None) -> int:
            s = dfs(node.left) + dfs(node.right) + node.val if node else 0
            subtree_sums.add(s)
            return s

        total = dfs(root)
        min_diff = float("inf")
        ans = 0
        for val in subtree_sums:
            if (diff := abs(total - val * 2)) < min_diff:
                min_diff = diff
                ans = val * (total - val)

        return ans % 1_000_000_007

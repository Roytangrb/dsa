# Author: RT
# Date: 2022-12-07T13:23:15.462Z
# URL: https://leetcode.com/problems/range-sum-of-bst/


from .types import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        ans = 0

        def dfs(root):
            if not root:
                return
            nonlocal ans
            if low <= root.val <= high:
                ans += root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val < low:
                dfs(root.right)
            else:
                dfs(root.left)

        dfs(root)
        return ans

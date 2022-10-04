# Author: RT
# Date: 2022-10-04T12:10:17.441Z
# URL: https://leetcode.com/problems/path-sum/


from .types import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node: TreeNode | None, rsum: int) -> bool:
            if node:
                rsum += node.val
                if not node.left and not node.right:
                    return rsum == targetSum
                else:
                    return dfs(node.left, rsum) or dfs(node.right, rsum)

            return False

        return dfs(root, 0)

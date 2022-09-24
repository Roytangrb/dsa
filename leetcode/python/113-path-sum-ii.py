# Author: RT
# Date: 2022-09-24T13:24:18.180Z
# URL: https://leetcode.com/problems/path-sum-ii/


from .types import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(node: TreeNode | None, s: int):
            if node:
                path.append(node.val)
                s += node.val

                if not node.left and not node.right:
                    if s == targetSum:
                        ans.append(list(path))

                if node.left:
                    dfs(node.left, s)

                if node.right:
                    dfs(node.right, s)

                path.pop()

        dfs(root, 0)
        return ans

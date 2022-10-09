# Author: RT
# Date: 2022-10-09T12:57:19.388Z
# URL: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


from .types import TreeNode


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        seen = set()

        def dfs(node):
            if node:
                ret = False
                ret |= dfs(node.left)
                ret |= dfs(node.right)
                ret |= k - node.val in seen
                seen.add(node.val)

                return ret

            return False

        return dfs(root)

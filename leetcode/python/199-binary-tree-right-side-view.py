# Author: RT
# Date: 2022-07-11T13:33:26.450Z
# URL: https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional

from .types import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        ans = []
        level = [root]
        while level:
            frontier = []
            for node in level:
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)

            ans.append(level[-1].val)
            level = frontier

        return ans

    def rightSideView__dfs(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        ans = []

        def dfs(node: TreeNode, level: int):
            if level == len(ans):
                ans.append(node.val)
            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 0)

        return ans

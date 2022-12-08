# Author: RT
# Date: 2022-12-08T14:05:09.755Z
# URL: https://leetcode.com/problems/leaf-similar-trees/

from itertools import zip_longest

from .types import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode) -> bool:
        def dfs(node: TreeNode | None):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return all(i == j for i, j in zip_longest(dfs(root1), dfs(root2)))

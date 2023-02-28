# Author: RT
# Date: 2023-02-28T14:46:22.051Z
# URL: https://leetcode.com/problems/find-duplicate-subtrees/

from collections import defaultdict

from .types import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        seen = defaultdict(list)

        def po(node: TreeNode | None):
            if node:
                tree = (node.val, po(node.left), po(node.right))
                seen[tree].append(node)
                return tree

        po(root)

        return [st[0] for st in seen.values() if st[1:]]

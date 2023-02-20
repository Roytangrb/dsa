# Author: RT
# Date: 2023-02-20T13:15:36.903Z
# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

from .types import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        q = deque([root] if root else [])
        reverse = True  # flag for next level
        while q:
            frontier = deque()
            out = []
            for node in q:
                out.append(node.val)
                children = [c for c in (node.left, node.right) if c]
                if reverse:
                    frontier.extendleft(children)
                else:
                    frontier.extendleft(reversed(children))

            ans.append(out)
            q = frontier
            reverse = not reverse

        return ans

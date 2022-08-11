# Author: RT
# Date: 2022-08-11T16:08:34.933Z
# URL: https://leetcode.com/problems/validate-binary-search-tree/


from .types import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = None
        node = root
        stack = []
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                curr = stack.pop()
                if prev is not None and curr.val <= prev:
                    return False

                prev = curr.val
                node = curr.right
            else:
                break

        return True

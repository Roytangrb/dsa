# Author: RT
# Date: 2022-11-15T13:42:25.084Z
# URL: https://leetcode.com/problems/count-complete-tree-nodes/


from .types import TreeNode


class Solution:
    def find_height(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        return self.find_height(node.left) + 1

    def path_exists(self, node: TreeNode, target: int, H: int) -> bool:
        l, r = 0, 2 ** (H - 1) - 1
        while H := H - 1:
            mid = l + (r - l) // 2
            if target <= mid:
                node = node.left
                r = mid
            else:
                node = node.right
                l = mid + 1
        return node is not None

    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        H = self.find_height(root)

        l, r = 0, 2 ** (H - 1) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if self.path_exists(root, mid, H):
                l = mid
            else:
                r = mid - 1

        return 2 ** (H - 1) + l

# Author: RT
# Date: 2023-06-15T02:33:34.407Z
# URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/


from .types import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q = [root] if root else []
        level = 1

        ans = 0
        ps = float("-inf")
        while q:
            frontier = []
            s = 0
            for node in q:
                s += node.val
                frontier.extend(filter(bool, [node.left, node.right]))

            if s > ps:
                ps = s
                ans = level

            q = frontier
            level += 1

        return ans

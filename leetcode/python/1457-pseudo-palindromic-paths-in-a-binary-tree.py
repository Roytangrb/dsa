# Author: RT
# Date: 2022-09-14T14:38:35.299Z
# URL: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/


from .types import TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        ans = 0

        def dfs(node: TreeNode | None, counter: list[int], odd_count: int):
            nonlocal ans

            if not node:
                return

            counter[node.val] += 1
            if counter[node.val] & 1:
                odd_count += 1
            else:
                odd_count -= 1

            if not node.left and not node.right:
                ans += odd_count <= 1

            dfs(node.left, counter, odd_count)
            dfs(node.right, counter, odd_count)

            # backtrack
            counter[node.val] -= 1

        dfs(root, [0] * 10, 0)

        return ans

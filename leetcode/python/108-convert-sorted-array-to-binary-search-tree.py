# Author: RT
# Date: 2022-08-10T13:43:15.026Z
# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from .types import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)

        def build(l, r):
            if l <= r:
                mid = l + (r - l) // 2
                return TreeNode(nums[mid], build(l, mid - 1), build(mid + 1, r))

            return None

        return build(0, n - 1)

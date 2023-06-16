# Author: RT
# Date: 2023-06-16T03:34:27.816Z
# URL: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/


from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        M = 1_000_000_007

        def build_tree(values: list[int]) -> int:
            """Returns number of ways to build the BST"""
            if not values:
                return 1

            left, right = [], []
            root = values[0]
            for num in values[1:]:
                if num < root:
                    left.append(num)
                else:
                    right.append(num)

            # values in left and right subtree can interleave while keeping
            # the values order intact within left and right subtree
            # i.e. Number of ways to interleave 2 ordered sequence (with length m and n)
            return (
                build_tree(left)
                * build_tree(right)
                * comb(len(left) + len(right), len(left))
                % M
            )

        return build_tree(nums) - 1  # the original nums order does not count as reorder

# Author: RT
# Date: 2022-07-10T16:01:57.837Z
# URL: https://leetcode.com/problems/range-sum-query-mutable/


class NumArray:
    """Array implmentation of segment tree for range sum"""

    def __init__(self, nums: list[int]):
        """Build segment tree"""
        n = len(nums)
        tree = [0] * (2 * n)

        # fill leaves with original values
        for i in range(n, 2 * n):
            tree[i] = nums[i - n]

        # build internal nodes bottom-up
        # first slot is empty
        for i in reversed(range(1, n)):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        self.tree = tree
        self.n = n

    def update(self, index: int, val: int) -> None:
        """Update value in segment tree"""
        # update original value in leaves
        index += self.n
        self.tree[index] = val

        # bubble up to update range sum changed
        while index:
            if index & 1:
                right = index
                left = right - 1
            else:
                left = index
                right = left + 1

            index //= 2  # parent node
            self.tree[index] = self.tree[left] + self.tree[right]

    def sumRange(self, left: int, right: int) -> int:
        """Query the the sum of a range"""
        # pos in the tree
        left += self.n
        right += self.n

        ans = 0
        while left <= right:
            # if left is a right child, parent contains values outside of range
            # add the value and point it to the node to the right of parent
            if left & 1:
                ans += self.tree[left]
                left += 1
            # Similarly, if right is a left child, parent contains values outside
            # of range, add the value and point it to the node to the left of parent
            if not right & 1:
                ans += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return ans

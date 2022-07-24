class SegmentTree:
    """Array implmentation of segment tree"""

    def __init__(self, n: int, values: list[int] | None = None) -> None:
        """Build segment tree

        Args:
            n: size of original values list
            values: initial values, default to zeros if not passed
        """
        self.n = n
        self.tree = [0] * (2 * n)
        if not values:
            return

        # fill leaves with original values
        for i in range(n, 2 * n):
            self.tree[i] = values[i - n]

        # build internal nodes bottom-up
        # first slot is empty
        for i in reversed(range(1, n)):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def get(self, index: int) -> int:
        """Get value by original index"""
        return self.tree[index + self.n]

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

    def sum_range(self, left: int, right: int) -> int:
        """Query the sum of a range"""
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

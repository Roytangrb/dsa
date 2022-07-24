class FenwickTree:
    """Array implmentation of Fenwick Tree (Binary Indexed Tree)"""

    def __init__(self, n: int, values: list[int] | None = None) -> None:
        """Build fenwick tree

        Args:
            n: size of original values list
            values: initial values, default to zeros if not passed
        """
        self.n = n
        self.tree = [0] * (n + 1)
        if not values:
            return

        # Build the Fenwick Tree with initial values, O(nlogn)
        for i, v in enumerate(values):
            self.add(i, v)

    def add(self, index: int, val: int) -> None:
        """Adding at orginal index and update affected range"""
        # index in BIT is 1 larger than index in original values
        index += 1
        while index < self.n + 1:
            self.tree[index] += val
            index += index & -index

    def sum_prefix(self, index: int) -> int:
        """Query the prefix sum (inclusive)

        Each element contains the sum of the values since its parent in the tree.
        """
        index += 1
        ans = 0
        while index:
            ans += self.tree[index]
            # unset the right-most set bit to find parent
            index &= index - 1

        return ans

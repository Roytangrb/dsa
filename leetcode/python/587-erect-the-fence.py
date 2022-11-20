# Author: RT
# Date: 2022-11-19T16:10:36.309Z
# URL: https://leetcode.com/problems/erect-the-fence/


import json
import sys
from itertools import chain


class Solution:
    """Find Convex Hull: https://en.wikipedia.org/wiki/Convex_hull"""

    def outerTrees(self, trees: list[list[int]]) -> list[tuple[int, int]]:
        trees.sort()
        lower_hull = []
        upper_hull = []
        for tree in trees:
            self.add_tree_to_hull(lower_hull, tree)
        for tree in reversed(trees):
            self.add_tree_to_hull(upper_hull, tree)

        # join lower and upper hulls and remove duplicate of leftmost & rightmost
        return list({tuple(t) for t in chain(lower_hull, upper_hull)})

    def add_tree_to_hull(self, hull: list[list[int]], tree: list[int]):
        """remove p1 if p2 -> p1 -> curr is a right turn (clockwise)"""
        while len(hull) >= 2 and self.cross_product(hull[-2], hull[-1], tree) < 0:
            hull.pop()
        hull.append(tree)

    def cross_product(self, a: list[int], b: list[int], c: list[int]) -> int:
        """cross product vector ->ab and ->bc"""
        ax, ay, bx, by, cx, cy = chain(a, b, c)
        vab = (by - ay, bx - ax)
        vbc = (cy - by, cx - bx)
        return vab[0] * vbc[1] - vab[1] * vbc[0]


if __name__ == "__main__":

    def viz(arr):
        """Visualize leetcode testcases"""
        m = max(x[1] for x in arr) + 1
        n = max(x[0] for x in arr) + 1
        g = [[" "] * n for _ in range(m)]
        for x, y in arr:
            g[y][x] = "O"
        for row in reversed(g):
            print(row)

    viz(json.loads(sys.argv[1]))

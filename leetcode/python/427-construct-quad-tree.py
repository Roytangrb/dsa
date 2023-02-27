# Author: RT
# Date: 2023-02-27T14:40:50.362Z
# URL: https://leetcode.com/problems/construct-quad-tree/


# Definition for a QuadTree node.
class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft: "Node" | None = None,
        topRight: "Node" | None = None,
        bottomLeft: "Node" | None = None,
        bottomRight: "Node" | None = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        n = len(grid)  # n = 2 ** x where 0 <= x <= 6
        self.grid = grid

        return self._construct(0, n - 1, 0, n - 1)

    def _construct(self, top: int, bottom: int, left: int, right: int) -> "Node":
        if top == bottom:
            return Node(val=self.grid[top][left], isLeaf=True)

        r = (bottom - top + 1) // 2
        sections = (
            self._construct(top, top + r - 1, left, left + r - 1),
            self._construct(top, top + r - 1, left + r, right),
            self._construct(top + r, bottom, left, left + r - 1),
            self._construct(top + r, bottom, left + r, right),
        )
        top_left, top_right, bottom_left, bottom_right = sections
        repr_v = top_left.val

        if all(sec.val == repr_v and sec.isLeaf for sec in sections):
            return Node(val=repr_v, isLeaf=True)
        else:
            return Node(
                val=0,
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right,
            )

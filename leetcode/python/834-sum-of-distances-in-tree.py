# Author: RT
# Date: 2022-12-22T16:02:32.644Z
# URL: https://leetcode.com/problems/sum-of-distances-in-tree/


from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class NaryTreeNode:
    val: int
    children: list = field(default_factory=list)
    subtree_size: int = 0


class Solution:
    def build_tree(self, n: int, edges: list[list[int]]) -> NaryTreeNode:
        """Build graph from edges and convert to a tree"""
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        treenodes = [NaryTreeNode(val=i) for i in range(n)]
        root = treenodes[0]  # pick any node as root
        # bfs build tree
        q = [root.val]
        seen = {root.val}
        while q:
            u = q.pop()
            for v in G[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
                    treenodes[u].children.append(treenodes[v])

        return root

    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        ans = [0] * n
        root = self.build_tree(n, edges)

        # optimization: this can be calc on bfs build tree
        # or, no need to convert to a directed tree. Just post-order traverse the
        # graph with any node as starting point
        def dfs1(node: NaryTreeNode | None, depth: int):
            """calc sum of distance from root to all nodes, and calc subtree size"""
            if not node:
                return 0

            ans[root.val] += depth
            node.subtree_size = 1
            for child in node.children:
                node.subtree_size += dfs1(child, depth + 1)

            return node.subtree_size

        def dfs2(node: NaryTreeNode, prev: int):
            """calc distance sum of current node base on parent's value"""
            # when descent from parent to current, distance sum decrease by
            # the current sub-tree size x, and increase by total size - x
            ans[node.val] = prev - node.subtree_size + (n - node.subtree_size)
            for child in node.children:
                dfs2(child, ans[node.val])

        dfs1(root, 0)
        for child in root.children:
            dfs2(child, ans[root.val])

        return ans

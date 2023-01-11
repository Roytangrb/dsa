# Author: RT
# Date: 2023-01-11T13:25:46.556Z
# URL: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/


from collections import defaultdict

from .types import NaryTreeNode


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

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        root = self.build_tree(n, edges)

        def dfs(node):
            if not node:
                return -1

            cs = [dfs(child) for child in node.children]

            curr = hasApple[node.val]
            if all(c == -1 for c in cs) and not curr:
                return -1

            return sum(c + 2 for c in cs if c > -1)

        return max(dfs(root), 0)

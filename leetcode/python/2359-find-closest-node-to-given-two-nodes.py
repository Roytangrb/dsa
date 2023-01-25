# Author: RT
# Date: 2023-01-25T14:11:23.075Z
# URL: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/


from collections import Counter, defaultdict


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        radj = defaultdict(list)

        for u, v in enumerate(edges):
            if v != -1:
                adj[u].append(v)
                radj[v].append(u)

        dist1 = Counter()
        dist2 = Counter()

        # given there is at most 1 outgoing edge for every node,
        # there is only 1 path between 2 nodes
        def dfs(node: int, dist: Counter, seen: set[int], d: int):
            if node not in seen:
                seen.add(node)
                dist[node] = d
                for u in adj[node]:
                    dfs(u, dist, seen, d + 1)

        dfs(node1, dist1, set(), 0)
        dfs(node2, dist2, set(), 0)

        return min(
            (candidate for candidate in dist1.keys() if candidate in dist2),
            key=lambda x: (max(dist1[x], dist2[x]), x),
            default=-1,
        )

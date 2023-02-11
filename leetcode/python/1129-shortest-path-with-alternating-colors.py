# Author: RT
# Date: 2023-02-11T10:37:43.258Z
# URL: https://leetcode.com/problems/shortest-path-with-alternating-colors/


from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        ANY, RED, BLUE = -1, 0, 1
        G = defaultdict(list)
        for u, v in redEdges:
            G[u].append((v, RED))
        for u, v in blueEdges:
            G[u].append((v, BLUE))

        q: deque[tuple[int, int, int]] = deque([(0, 0, ANY)])
        used_edges = set()
        ans = [-1] * n
        while q:
            u, dist, prev_color = q.popleft()
            # update shortest distance on first visit, but allow same
            # node to be visited again to change color
            if ans[u] == -1:
                ans[u] = dist

            for v, color in G[u]:
                if (u, v, color) not in used_edges and color != prev_color:
                    used_edges.add((u, v, color))
                    q.append((v, dist + 1, color))

        return ans

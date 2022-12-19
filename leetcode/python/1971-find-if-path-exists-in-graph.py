# Author: RT
# Date: 2022-12-19T12:14:02.122Z
# URL: https://leetcode.com/problems/find-if-path-exists-in-graph/


from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        q = [source]
        visited = {source}
        while q:
            nq = []
            for u in q:
                if u == destination:
                    return True
                for v in G[u]:
                    if v not in visited:
                        nq.append(v)
                        visited.add(v)

            q = nq

        return False

# Author: RT
# Date: 2023-07-12T04:44:43.533Z
# URL: https://leetcode.com/problems/find-eventual-safe-states/

from collections import Counter, defaultdict


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # O(V + E) topological sort
        n = len(graph)
        radj = defaultdict(list)
        indegree = Counter()
        term_nodes = []
        for u, vs in enumerate(graph):
            # when out-degree of original graph node is zero
            if not vs:
                term_nodes.append(u)

            # construct new graph with edges revsered, for
            # removing edges from term/safe nodes
            for v in vs:
                radj[v].append(u)
                indegree[u] += 1

        ans = []
        q = term_nodes
        while q:
            frontier = []
            for safe_node in q:
                ans.append(safe_node)
                for v in radj[safe_node]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        frontier.append(v)

            q = frontier

        return sorted(ans)

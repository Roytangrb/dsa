# Author: RT
# Date: 2023-05-20T04:55:10.087Z
# URL: https://leetcode.com/problems/evaluate-division/


from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        adj = defaultdict(list)
        quotients = {}

        for v, e in zip(values, equations):
            a, b = e
            quotients[(a, b)] = v
            quotients[(b, a)] = 1 / v  # given v is not zero
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, dest, visited, v):
            if node not in adj or dest not in adj:
                return -1

            if node == dest:
                return v

            if node in visited:
                return -1

            visited.add(node)
            return next(
                (
                    ret
                    for neighbor in adj[node]
                    if (
                        ret := dfs(
                            neighbor, dest, visited, v * quotients[(node, neighbor)]
                        )
                    )
                    >= 0
                ),
                -1,
            )

        return [dfs(src, dest, set(), 1) for src, dest in queries]

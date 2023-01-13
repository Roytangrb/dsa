# Author: RT
# Date: 2023-01-13T13:54:29.410Z
# URL: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/


from collections import Counter, defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        n = len(labels)
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        seen = set()
        ans = [0] * n

        def dfs(i: int) -> Counter:
            seen.add(i)
            c = Counter()
            for child in adj[i]:
                if child not in seen:
                    c += dfs(child)

            label = labels[i]
            c[label] += 1
            ans[i] = c[label]
            return c

        dfs(0)

        return ans

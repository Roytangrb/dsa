# Author: RT
# Date: 2023-05-18T05:23:46.849Z
# URL: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/


from collections import Counter


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indegree = Counter()
        for u, v in edges:
            indegree[v] += 1

        return [u for u in range(n) if indegree[u] == 0]

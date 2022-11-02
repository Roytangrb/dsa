# Author: RT
# Date: 2022-11-02T12:56:55.473Z
# URL: https://leetcode.com/problems/minimum-genetic-mutation/


from collections import defaultdict


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        try:
            T = bank.index(end)
        except ValueError:
            return -1

        S = 0
        if start not in bank:
            S = len(bank)
            bank.append(start)
        else:
            S = bank.index(start)

        G = defaultdict(set)
        n = len(bank)
        for u in range(n):
            for v in range(u + 1, n):
                if self.distance(bank[u], bank[v]) == 1:
                    G[u].add(v)
                    G[v].add(u)

        # bfs shortest path
        q = [T]
        seen = set()
        ans = 0
        while q:
            frontier = []
            for node in q:
                if node == S:
                    return ans

                seen.add(node)
                for neighbor in G[node]:
                    if neighbor not in seen:
                        frontier.append(neighbor)

            ans += 1
            q = frontier

        return -1

    def distance(self, a: str, b: str) -> int:
        return sum(int(ca != cb) for ca, cb in zip(a, b))

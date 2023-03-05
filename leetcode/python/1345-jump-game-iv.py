# Author: RT
# Date: 2023-03-05T09:57:01.311Z
# URL: https://leetcode.com/problems/jump-game-iv/


from collections import defaultdict, deque
from itertools import chain


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        values = defaultdict(list)
        for i, val in enumerate(arr):
            values[val].append(i)

        n = len(arr)
        step = 0
        visited = {0}
        q = deque([0])

        while q:
            frontier = []

            for u in q:
                if u == n - 1:
                    return step

                neighbors = filter(lambda x: 0 <= x < n, [u + 1, u - 1])
                for v in chain(values[arr[u]], neighbors):
                    if v not in visited:
                        visited.add(v)
                        frontier.append(v)

                values[arr[u]].clear()

            q = frontier
            step += 1

        return step

# Author: RT
# Date: 2023-06-13T03:14:57.713Z
# URL: https://leetcode.com/problems/equal-row-and-column-pairs/


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trie = {}
        for r, row in enumerate(grid):
            t = trie
            for num in row:
                t[num] = t.get(num, {})
                t = t[num]
            t[r] = True

        ans = 0
        for i in range(n):
            t = trie
            for row in grid:
                if row[i] in t:
                    t = t[row[i]]
                else:
                    break
            else:
                ans += len(t.keys())

        return ans

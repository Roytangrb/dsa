# Author: RT
# Date: 2023-06-11T05:25:43.807Z
# URL: https://leetcode.com/contest/weekly-contest-349/problems/collecting-chocolates/


class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        n = len(nums)
        mc = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            mc[i][0] = nums[i]
        for i in range(n):
            for j in range(1, n):
                mc[i][j] = min(mc[i][j - 1], nums[(i + j) % n])

        def solve(max_shifts):
            ans = 0
            for i in range(n):
                ans += mc[i][max_shifts]

            return ans + x * max_shifts

        return min(solve(m) for m in range(n))

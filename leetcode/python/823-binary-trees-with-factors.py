# Author: RT
# Date: 2022-08-09T16:21:44.157Z
# URL: https://leetcode.com/problems/binary-trees-with-factors/


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        M = 1_000_000_007
        # arr contains unique int > 1
        arr.sort()
        vi = {v: i for i, v in enumerate(arr)}

        # dp[i]: number of tree with arr[i] as root
        dp = [1] * len(arr)
        ans = 0
        for i, root in enumerate(arr):
            for j in range(i):  # exclude i because i = i * 1
                quotient, remainder = divmod(root, arr[j])
                if not remainder and quotient in vi:
                    dp[i] = (dp[i] + dp[j] * dp[vi[quotient]]) % M

            ans = (ans + dp[i]) % M

        return ans

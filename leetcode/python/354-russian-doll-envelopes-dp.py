# Author: RT
# Date: 2022-05-25T15:26:47.837Z
# URL: https://leetcode.com/problems/russian-doll-envelopes/


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # convert problem to longest increasing subsequence (LIS) size
        envelopes.sort(key=lambda x: (x[0], x[1]))

        n = len(envelopes)

        # longest subsequence ending at i
        dp = [1] * n

        for i in range(1, n):
            wi, hi = envelopes[i]
            for j in range(i):
                wj, hj = envelopes[j]
                if wi > wj and hi > hj:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

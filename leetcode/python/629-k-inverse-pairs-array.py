# Author: RT
# Date: 2022-07-17T17:18:08.015Z
# URL: https://leetcode.com/problems/k-inverse-pairs-array/


from functools import cache


class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if not n:
            return 0
        if not k:
            return 1
        ans = 0
        for i in range(min(k + 1, n)):
            ans = (ans + self.kInversePairs(n - 1, k - i)) % 1_000_000_007

        return ans

    def kInversePairs__bottom_up(self, n: int, k: int) -> int:
        M = 1_000_000_007

        # Optimized with cumulative sum
        ans = 1
        prefix_sum_prev = [0] * (k + 1)

        for i in range(1, n + 1):
            prefix_sum_curr = [0] * (k + 1)
            prefix_sum_curr[0] = 1
            for j in range(1, k + 1):
                ans = prefix_sum_prev[j]
                if j >= i:
                    ans = (ans + M - prefix_sum_prev[j - i]) % M
                prefix_sum_curr[j] = (prefix_sum_curr[j - 1] + ans) % M

            prefix_sum_prev = prefix_sum_curr

        return ans

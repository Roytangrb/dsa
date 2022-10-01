# Author: RT
# Date: 2022-10-01T08:45:14.747Z
# URL: https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.dp(s)

    def dp(self, s: str) -> int:
        n = len(s)
        # ways to decode substring start at i (s[i:])
        # could be compressed to constant space, only dp[i+1] and dp[i+2] are needed
        dp = [1] * (n + 1)  # base case i == n is 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]  # use single digit
            # use 2 digits
            if s[i] == "1" and i < n - 1:
                dp[i] += dp[i + 2]
            if s[i] == "2" and i < n - 1 and int(s[i + 1]) < 7:
                dp[i] += dp[i + 2]

        return dp[0]

    def backtrack(self, s: str) -> int:
        ans = 0
        n = len(s)

        def decode(i):
            nonlocal ans
            if i == n:
                ans += 1
                return

            c1 = s[i]
            if c1 == "0":
                return
            if c1 == "1" and i < n - 1:
                decode(i + 2)
            elif c1 == "2" and i < n - 1 and int(s[i + 1]) < 7:
                decode(i + 2)

            decode(i + 1)

        decode(0)
        return ans

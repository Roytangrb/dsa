# Author: RT
# Date: 2022-07-07T17:00:47.105Z
# URL: https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)

        if m + n != o:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # i: prefix length used from s1
                # j: prefix length used from s2
                if not i and not j:
                    dp[i][j] = True
                elif not i:
                    dp[i][j] = dp[0][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif not j:
                    dp[i][j] = dp[i - 1][0] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        # 2d DP, only the cells to the left and above are needed, can bt compressed to 1d DP
        return dp[m][n]

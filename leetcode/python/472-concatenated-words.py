# Author: RT
# Date: 2023-01-27T05:08:09.162Z
# URL: https://leetcode.com/problems/concatenated-words/


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        ans = []
        ws = frozenset(words)

        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                dp[i] = any(
                    dp[j] and word[j:i] in ws
                    for j in range(
                        0 if i != n else 1,  # exclude the current word itself
                        i,
                    )
                )

            if dp[n]:
                ans.append(word)

        return ans

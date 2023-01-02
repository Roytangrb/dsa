# Author: RT
# Date: 2023-01-02T06:09:49.515Z
# URL: https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(1 for c in word if c.upper() == c)
        return (
            count == len(word)
            or count == 0
            or (count == 1 and word[0].upper() == word[0])
        )

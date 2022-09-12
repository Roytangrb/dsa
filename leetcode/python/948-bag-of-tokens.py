# Author: RT
# Date: 2022-09-12T05:56:55.337Z
# URL: https://leetcode.com/problems/bag-of-tokens/


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        score = 0
        while l < r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif score:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break

        if l == r:
            score += power >= tokens[l]

        return score

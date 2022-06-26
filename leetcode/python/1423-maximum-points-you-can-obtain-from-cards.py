# Author: RT
# Date: 2022-06-26T12:57:59.270Z
# URL: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # max of head + tail = total - min subarray sum
        n = len(cardPoints)
        z = n - k
        window = sum(cardPoints[:k])
        l, r = 0, z
        min_window = window
        total = window
        while r < n:
            window = window + cardPoints[r] - cardPoints[l]
            total += cardPoints[r]
            l += 1
            r += 1
            min_window = min(min_window, window)

        return total - min_window

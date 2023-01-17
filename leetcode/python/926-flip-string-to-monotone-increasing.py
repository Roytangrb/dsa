# Author: RT
# Date: 2023-01-17T14:32:04.567Z
# URL: https://leetcode.com/problems/flip-string-to-monotone-increasing/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Two pass using dynamic window (left with only 0s and right with only 1s)"""
        ones_on_left = 0
        zeros_on_right = s.count("0")
        ans = zeros_on_right
        for c in s:
            if c == "0":
                zeros_on_right -= 1
            else:
                ones_on_left += 1

            ans = min(ans, ones_on_left + zeros_on_right)

        return ans

    def minFlipsMonoIncr__dp(self, s: str) -> int:
        """DP - transition appending current char to monotone prefix"""
        ans = 0
        ones = 0
        for c in s:
            if c == "0":
                # flip all previous 1s to 0s
                # or flip current bit to 1
                ans = min(ones, ans + 1)
            else:
                ones += 1

        return ans

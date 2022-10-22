# Author: RT
# Date: 2022-10-22T14:04:09.427Z
# URL: https://leetcode.com/problems/minimum-window-substring/


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        l = r = 0

        t_freq = Counter(t)
        t_char_count = len(t_freq)
        formed = 0

        ans = ""
        freq = Counter()
        while r < n:
            c = s[r]
            freq[c] += 1
            if freq[c] == t_freq[c]:
                formed += 1
                while formed == t_char_count:
                    if not ans or (r - l + 1) < len(ans):
                        ans = s[l : r + 1]
                    freq[s[l]] -= 1
                    if freq[s[l]] < t_freq[s[l]]:
                        formed -= 1
                    l += 1
            r += 1

        return ans

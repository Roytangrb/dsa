# Author: RT
# Date: 2022-11-03T14:55:45.211Z
# URL: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/


from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        ans = 0
        wc = Counter(words)

        has_center = 0
        for word in wc.keys():
            rword = word[::-1]
            if word[0] == word[1]:
                if wc[word] & 1:
                    has_center = 1

                pairs = wc[word] // 2
                ans += 2 * pairs
                wc[word] -= pairs
            elif rword in wc:
                pairs = min(wc[word], wc[rword])
                ans += 2 * pairs
                wc[word] -= pairs
                wc[rword] -= pairs

        return (ans + has_center) * 2

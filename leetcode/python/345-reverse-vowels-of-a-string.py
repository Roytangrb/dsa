# Author: RT
# Date: 2022-11-04T16:56:16.845Z
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        l, r = 0, len(s) - 1
        s = list(s)
        is_vowel = lambda i: s[i] in vowels
        while l < r:
            if is_vowel(l) and is_vowel(r):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                continue
            if not is_vowel(l):
                l += 1
            if not is_vowel(r):
                r -= 1

        return "".join(s)

# Author: RT
# Date: 2022-10-10T12:50:20.758Z
# URL: https://leetcode.com/problems/break-a-palindrome/


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        pos_not_a = -1
        for i in range(n // 2):  # changing the odd center will not break palindrome
            if ord(palindrome[i]) > ord("a"):
                pos_not_a = i
                break

        if pos_not_a == -1:
            return palindrome[: n - 1] + "b"
        else:
            return palindrome[:pos_not_a] + "a" + palindrome[pos_not_a + 1 :]

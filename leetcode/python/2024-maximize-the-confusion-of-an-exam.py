# Author: RT
# Date: 2023-07-07T02:19:46.391Z
# URL: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l = cnt_t = cnt_f = ans = 0
        for r, c in enumerate(answerKey):
            cnt_t += c == "T"
            cnt_f += c == "F"
            while cnt_t > k and cnt_f > k:
                remove = answerKey[l]
                cnt_t -= remove == "T"
                cnt_f -= remove == "F"
                l += 1

            ans = max(ans, r - l + 1)

        return ans

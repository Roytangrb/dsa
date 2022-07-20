# Author: RT
# Date: 2022-07-20T15:15:49.550Z
# URL: https://leetcode.com/problems/number-of-matching-subsequences/


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Iterate S only once, maintain list of queues for the next character
        # each word needs to match
        ans = 0
        queues = [[] for _ in range(26)]

        # place word in initial queue
        for word in words:
            it = iter(word)
            queues[ord(next(it)) - ord("a")].append(it)

        for c in s:
            i = ord(c) - ord("a")
            curr = queues[i]
            queues[i] = []
            for it in curr:
                if next_c := next(it, None):
                    queues[ord(next_c) - ord("a")].append(it)
                else:
                    ans += 1

        return ans

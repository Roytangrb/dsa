# Author: RT
# Date: 2022-10-19T14:32:58.098Z
# URL: https://leetcode.com/problems/top-k-frequent-words/


from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return [
            word for _, word in sorted([(-c, w) for w, c in Counter(words).items()])[:k]
        ]

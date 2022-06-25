# Author: RT
# Date: 2022-06-25T15:44:23.427Z
# URL: https://leetcode.com/problems/short-encoding-of-words/

from collections import defaultdict
from functools import reduce


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # remove words that are suffix of another word
        # dedup
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        nodes = [reduce(dict.__getitem__, reversed(word), trie) for word in words]

        # count word if ends at a leave node
        return sum(len(word) + 1 for i, word in enumerate(words) if not len(nodes[i]))

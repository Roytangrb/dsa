# Author: RT
# Date: 2022-06-18T07:47:42.607Z
# URL: https://leetcode.com/problems/prefix-and-suffix-search/

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Node:
    children: dict[str, "Node"]
    char: str
    words: list[int]


class WordFilter:
    def __init__(self, words: list[str]):
        self.ptrie, self.strie = {}, {}

        node_cache = {}
        for i, word in enumerate(words):
            if word in node_cache:
                node_cache[word][0].words.append(i)
                node_cache[word][1].words.append(i)
                continue

            pn = self.insert_word(word, i)
            sn = self.insert_word(word, i, reverse=True)
            node_cache[word] = (pn, sn)

    def insert_word(self, word: str, i: int, reverse: bool = False) -> Node:
        w = reversed(word) if reverse else word
        t = self.strie if reverse else self.ptrie

        node = None
        for c in w:
            if c in t:
                t[c].words.append(i)
            else:
                t[c] = Node({}, c, [i])
            node = t[c]
            t = t[c].children

        return node  # type: ignore

    def find_words(self, prefix: Iterable, trie: dict) -> list[int]:
        node = None
        t = trie
        for c in prefix:
            if c not in t:
                return []
            node = t[c]
            t = t[c].children

        return node.words if node else []

    def f(self, prefix: str, suffix: str) -> int:
        pw = self.find_words(prefix, self.ptrie)
        sw = self.find_words(reversed(suffix), self.strie)
        i, j = len(pw) - 1, len(sw) - 1

        while i >= 0 and j >= 0:
            if pw[i] == sw[j]:
                return pw[i]
            elif pw[i] > sw[j]:
                i -= 1
            else:
                j -= 1
        return -1

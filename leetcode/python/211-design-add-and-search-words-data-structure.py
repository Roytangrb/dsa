# Author: RT
# Date: 2023-03-19T10:08:24.996Z
# URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/


class WordDictionary:
    END_OF_WORD_FLAG = "EOW"
    trie: dict

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node[self.END_OF_WORD_FLAG] = True

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word)

    def dfs(self, trie: dict, word: str) -> bool:
        for i, c in enumerate(word):
            if c == ".":
                w = word[i + 1 :]
                return any(
                    (
                        self.dfs(t, w)
                        for k, t in trie.items()
                        if k != self.END_OF_WORD_FLAG
                    )
                )

            if c not in trie:
                return False

            trie = trie[c]

        return self.END_OF_WORD_FLAG in trie

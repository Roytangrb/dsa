# Author: RT
# Date: 2022-11-05T16:37:31.283Z
# URL: https://leetcode.com/problems/word-search-ii/


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        self.board = board
        self.ans = []
        trie = self._build_trie(words)
        self.trie = trie

        for i in range(len(board)):
            for j in range(len(board[0])):
                self._search_trie(i, j, trie, [], set())

        return self.ans

    def _search_trie(self, i: int, j: int, t: dict, cs: list[str], visited: set):
        c = self.board[i][j]
        if c in t and (i, j) not in visited:
            cs.append(c)
            visited.add((i, j))
            is_word_end = t[c][1]
            if is_word_end:
                # mark word found to avoid duplicates and allow pruning
                t[c] = (t[c][0], False)
                self.ans.append("".join(cs))

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]):
                    self._search_trie(x, y, t[c][0], cs, visited)

            cs.pop()
            visited.remove((i, j))

            # Optimization: prune trie recursively by removing leaf node which
            # is not word end
            if not t[c][0] and not t[c][1]:
                del t[c]

    def _build_trie(self, words: list[str]) -> dict:
        trie = {}
        for word in words:
            t = trie
            for i, c in enumerate(word):
                if c not in t:
                    t[c] = ({}, False)
                t[c] = (t[c][0], t[c][1] or i == len(word) - 1)
                t = t[c][0]

        return trie

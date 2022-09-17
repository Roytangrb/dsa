# Author: RT
# Date: 2022-09-17T12:58:09.125Z
# URL: https://leetcode.com/problems/palindrome-pairs/


from typing import Iterable


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # O(nmm) where n is number of words and m is length of words
        # NOTE: this solution is not accepted when word is long with repeated chars
        self.trie = {}
        self.epsilon = None
        for i, word in enumerate(words):
            self.trie_add(word, i)
            if not len(word):
                self.epsilon = i

        ans = []
        # for every word, try center at every position
        for i, word in enumerate(words):
            n = len(word)
            if i == self.epsilon:
                continue
            # no center case
            if (j := self.trie_index_of(reversed(word))) is not None and i != j:
                ans.append([i, j])

            for center in range(n):
                l = r = center
                is_center_valid = True
                while l >= 0 and r < n:
                    if word[l] != word[r]:
                        is_center_valid = False
                        break
                    l -= 1
                    r += 1
                if not is_center_valid:
                    continue
                if l == -1 and r == n:
                    # word itself is a palindrome
                    if self.epsilon is not None:
                        ans.append([self.epsilon, i])
                        ans.append([i, self.epsilon])
                elif l == -1:
                    if (j := self.trie_index_of(reversed(word[r:]))) is not None:
                        ans.append([j, i])
                elif r == n:
                    if (j := self.trie_index_of(reversed(word[: l + 1]))) is not None:
                        ans.append([i, j])

            for center in range(n - 1):
                l, r = center, center + 1
                is_center_valid = True
                while l >= 0 and r < n:
                    if word[l] != word[r]:
                        is_center_valid = False
                        break
                    l -= 1
                    r += 1
                if not is_center_valid:
                    continue
                if l == -1 and r == n:
                    # word itself is a palindrome
                    if self.epsilon is not None:
                        ans.append([self.epsilon, i])
                        ans.append([i, self.epsilon])
                elif l == -1:
                    if (j := self.trie_index_of(reversed(word[r:]))) is not None:
                        ans.append([j, i])
                elif r == n:
                    if (j := self.trie_index_of(reversed(word[: l + 1]))) is not None:
                        ans.append([i, j])
        return ans

    def trie_add(self, word: str, idx: int):
        n = len(word)
        t = self.trie
        for i, c in enumerate(word):
            if c not in t:
                t[c] = [{}, None]  # children and word index (unique)
            if t[c][1] is None and i == n - 1:
                t[c][1] = idx
            t = t[c][0]

    def trie_index_of(self, word: Iterable[str]) -> int | None:
        t = self.trie
        idx = None
        for c in word:
            if c not in t:
                return None
            idx = t[c][1]
            t = t[c][0]

        return idx

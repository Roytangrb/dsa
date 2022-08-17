# Author: RT
# Date: 2022-08-14T17:05:52.129Z
# URL: https://leetcode.com/problems/word-ladder-ii/


from collections import defaultdict


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        n = len(wordList)
        adj = defaultdict(set)
        for word in wordList:
            if self.is_connected(beginWord, word):
                adj[beginWord].add(word)
                adj[word].add(beginWord)

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_connected(wordList[i], wordList[j]):
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])

        if endWord not in adj:
            return []

        # BFS shortest path
        ans = []
        seen = {beginWord}
        paths = [[beginWord]]
        q = [beginWord]
        while q and endWord not in seen:
            _q = []
            _paths = []
            # all paths need to be found, update seen after finish processing each level
            _seen = set()
            for i, u in enumerate(q):
                for v in adj[u]:
                    if v not in seen:
                        _seen.add(v)
                        _q.append(v)
                        _paths.append(paths[i] + [v])
                        if v == endWord:
                            ans.append(_paths[-1])
            q.clear()
            q = _q
            paths.clear()
            paths = _paths
            seen |= _seen

        return ans

    def is_connected(self, w1: str, w2: str) -> bool:
        diff = False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                if diff:
                    return False
                diff = True

        return True

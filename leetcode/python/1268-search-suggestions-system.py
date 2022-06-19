# Author: RT
# Date: 2022-06-19T17:00:33.640Z
# URL: https://leetcode.com/problems/search-suggestions-system/

import bisect


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        trie = {}
        for p in products:
            t = trie
            for c in p:
                if c not in t:
                    t[c] = ({}, [p])
                else:
                    bisect.insort(t[c][1], p)
                t = t[c][0]

        ans, t = [], trie
        for c in searchWord:
            if c in t:
                ans.append(t[c][1][:3])
                t = t[c][0]
            else:
                ans.append([])
                t = {}

        return ans

# Author: RT
# Date: 2022-10-28T15:27:55.864Z
# URL: https://leetcode.com/problems/group-anagrams/


from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        myhash = lambda x: tuple(sorted(Counter(x).items()))
        groups = defaultdict(list)
        for s in strs:
            sid = myhash(s)
            groups[sid].append(s)

        return list(groups.values())

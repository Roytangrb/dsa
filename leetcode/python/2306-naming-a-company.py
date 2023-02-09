# Author: RT
# Date: 2023-02-09T14:02:40.127Z
# URL: https://leetcode.com/problems/naming-a-company/


from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        initial_groups = defaultdict(set)
        for word in ideas:
            initial_groups[word[0]].add(hash(word[1:]))

        initials = list(initial_groups.keys())
        m = len(initials)
        ans = 0
        for i in range(m):
            for j in range(i + 1, m):
                a, b = initials[i], initials[j]
                suffices_a, suffices_b = initial_groups[a], initial_groups[b]
                mutual = len(suffices_a & suffices_b)
                ans += (len(suffices_a) - mutual) * (len(suffices_b) - mutual) * 2

        return ans

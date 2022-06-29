# Author: RT
# Date: 2022-06-29T14:32:40.850Z
# URL: https://leetcode.com/problems/queue-reconstruction-by-height/


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda d: (-d[0], d[1]))

        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans

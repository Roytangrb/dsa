# Author: RT
# Date: 2023-01-23T16:32:13.826Z
# URL: https://leetcode.com/problems/find-the-town-judge/


from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        judge_can = set(range(1, n + 1))
        count = Counter()
        for ter, tee in trust:
            if ter in judge_can:
                judge_can.remove(ter)
            count[tee] += 1

        return next((i for i in judge_can if count[i] == n - 1), -1)

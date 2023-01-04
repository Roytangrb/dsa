# Author: RT
# Date: 2023-01-04T14:10:46.192Z
# URL: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/


from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        return max(
            sum(
                count // 3 + (count % 3 != 0) if count > 1 else float("-inf")
                for count in Counter(tasks).values()
            ),
            -1,
        )

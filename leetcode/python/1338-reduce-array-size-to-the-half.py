# Author: RT
# Date: 2022-08-18T14:10:45.506Z
# URL: https://leetcode.com/problems/reduce-array-size-to-the-half/


from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = Counter(arr)
        total = sum(counts.values())
        remain = total
        ans = 0
        for _, freq in counts.most_common():
            if remain * 2 <= total:
                break
            remain -= freq
            ans += 1

        return ans

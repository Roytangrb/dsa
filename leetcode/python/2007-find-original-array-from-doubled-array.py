# Author: RT
# Date: 2022-09-15T13:33:30.905Z
# URL: https://leetcode.com/problems/find-original-array-from-doubled-array/


from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        n = len(changed)
        if n & 1:
            return []

        changed.sort(reverse=True)
        c = Counter(changed)
        original = []
        for num in changed:
            if not c[num]:
                continue

            c[num] -= 1
            # list are sorted descending, when we process num, there
            # are no available bigger value to be its double, so num
            # has to be a doubled value when it's even
            if num & 1:
                original.append(num)
            else:
                if c[num // 2]:
                    c[num // 2] -= 1
                    original.append(num // 2)
                else:
                    return []

        return original if len(original) * 2 == n else []

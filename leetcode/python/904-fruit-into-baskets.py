# Author: RT
# Date: 2023-02-07T12:47:07.569Z
# URL: https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)

        seen = [fruits[0]]
        l = 0
        ft1 = 0  # end position (inclusive) of the 1st fruit type
        ans = 1
        for r in range(1, n):
            curr = fruits[r]
            if curr == seen[0]:
                # when xxxooox, discard prefix of 1st type
                if len(seen) == 2:
                    ft1 = r - 1
                    seen = [seen[1], curr]
                # when xxxx, extend end of 1st type
                else:
                    ft1 = r

            if curr not in seen:
                # when xxxoooi, discard prefix of 1st type
                if len(seen) == 2:
                    seen.pop(0)
                    l = ft1 + 1
                    ft1 = r - 1
                # when xxxo, add current type as second
                seen.append(curr)

            # record running max, with r as the last collected tree
            ans = max(ans, r - l + 1)

        return ans

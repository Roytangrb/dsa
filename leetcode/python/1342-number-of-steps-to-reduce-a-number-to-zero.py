# Author: RT
# Date: 2022-05-27T16:40:36.350Z
# URL: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0

        while num:
            if num & 1:
                # count the step to subtract 1
                ans += 1

            # divide by 2
            num >>= 1
            ans += 1

        # last bit's step counted twice
        # if no set bit return 0
        return max(ans - 1, 0)

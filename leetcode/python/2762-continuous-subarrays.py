# Author: RT
# Date: 2023-07-02T17:59:36.635Z
# URL: https://leetcode.com/problems/continuous-subarrays/description/


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1
        l = 0
        # there could only be 3 uniq nums in win
        win = {nums[0]: 0}
        sm = lg = nums[0]
        for r in range(1, n):
            num = nums[r]
            if abs(num - sm) > 2 or abs(num - lg) > 2:
                pops = []
                for seen, last_pos in win.items():
                    if abs(seen - num) > 2:
                        l = max(l, last_pos + 1)
                        pops.append(seen)
                for p in pops:
                    win.pop(p)

            ans += r - l + 1
            win[num] = r
            sm = min(win.keys())
            lg = max(win.keys())

        return ans

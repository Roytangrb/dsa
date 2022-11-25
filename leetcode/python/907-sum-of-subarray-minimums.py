# Author: RT
# Date: 2022-11-25T14:45:18.963Z
# URL: https://leetcode.com/problems/sum-of-subarray-minimums/


from itertools import chain


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """Constraint: 1 <= arr[i] <= 3 * 10**4"""
        M = 1_000_000_007
        # Idea: instead of generate all subarray O(n2) and find min
        # in each subarray, find each arr[i]'s contribution to final
        # result, i.e.,
        # {number of subarray where arr[i] is the min} * arr[i]
        stack = []
        ans = 0
        for k, num in enumerate(chain(arr, [0])):
            while stack and num <= stack[-1][1]:
                j, _ = stack.pop()
                i = stack[-1][0] if stack else -1
                # arr[i+1:k] is where arr[k] is min
                # number of subarray containing arr[j] in arr[i+1:k] =
                subarray_count = (j - i) * (k - j)
                ans = (ans + subarray_count * arr[j]) % M

            stack.append((k, num))

        return ans

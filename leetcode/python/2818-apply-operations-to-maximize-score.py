# Author: RT
# Date: 2023-08-13T19:48:39.859Z
# URL: https://leetcode.com/problems/apply-operations-to-maximize-score/


from functools import cache


@cache
def count_dis_prime_factors(n):
    """Count number of distinct prime factors"""
    i = 2
    fc = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fc.add(i)
    if n > 1:
        fc.add(n)
    return len(fc)


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        M = 10**9 + 7
        ans = 1
        scores = [count_dis_prime_factors(num) for num in nums]
        # For each nums[i], find l, r such that sub-arrays of nums[l:r+1] containing
        # nums[i] and nums[i] is the leftmost highest scored number.
        # Use stack to pre-compute l, r for every in O(n) time.
        stack = []
        i_l_map, i_r_map = {}, {}
        for i, score in enumerate(scores):
            while stack and score > stack[-1][0]:
                top_i = stack.pop()[1]
                i_r_map[top_i] = i - 1
                i_l_map[i] = top_i

            i_l_map[i] = stack[-1][1] + 1 if stack else 0
            stack.append((score, i))

        for i, num in sorted(enumerate(nums), key=lambda x: x[1], reverse=True):
            ms = scores[i]
            # Right bound of remaining elements in stack is the last position of nums
            l, r = i_l_map[i], i_r_map.get(i, n - 1)
            # sub-array ending at i + sub-array starting at i
            subarray_count = (i - l + 1) + (r - i + 1) - 1
            # sub-array containing i
            subarray_count += (i - l) * (r - i)

            use = min(k, subarray_count)
            ans = ans * (num**use) % M

            k -= use
            if not k:
                break

        return ans

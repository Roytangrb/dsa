# Author: RT
# Date: 2023-07-02T18:44:06.998Z
# URL: https://leetcode.com/problems/prime-pairs-with-target-sum/description/


def generate_primes(n: int) -> list[bool]:
    if n < 2:
        return [False] * (n + 1)

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    # If a number could be factored, n = a * b, if b >= sqrt(n),
    # then a <= sqrt(n), we don't need to mark multiples of b
    # because they have already been marked as multiple of a at this point.
    while p * p <= n:
        if is_prime[p]:
            i = 2
            while i * p <= n:
                is_prime[i * p] = False
                i += 1

        p += 1

    return is_prime


class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        is_prime = generate_primes(n)
        ans = []
        for i in range(1, n // 2 + 1):
            if is_prime[i] and is_prime[n - i]:
                ans.append([i, n - i])

        return ans

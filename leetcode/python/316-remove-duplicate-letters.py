# Author: RT
# Date: 2023-09-26T23:47:12.835Z
# URL: https://leetcode.com/problems/remove-duplicate-letters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and last_seen[stack[-1]] > i:
                    visited.remove(stack.pop())

                stack.append(c)
                visited.add(c)
            # if c is already added to the stack before, ignore. If there are some
            # lexicographically smaller sequence x could be formed between handling
            # the second and the first occurrences of c, the first occurrence of c
            # would have been popped out of the stack earlier.

        return "".join(stack)

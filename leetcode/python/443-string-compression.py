# Author: RT
# Date: 2023-03-02T12:13:06.871Z
# URL: https://leetcode.com/problems/string-compression/


from itertools import chain


class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        prev = chars[0]
        count = 0
        for c in chain(chars, [""]):
            if c == prev:
                count += 1
            else:
                chars[i] = prev
                i += 1
                if count > 1:
                    for d in str(count):
                        chars[i] = d
                        i += 1

                count = 1
                prev = c

        return i

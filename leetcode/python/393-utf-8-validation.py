# Author: RT
# Date: 2022-09-13T14:02:50.199Z
# URL: https://leetcode.com/problems/utf-8-validation/


class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        n = len(data)
        l1 = 1 << 7
        l2 = 1 << 6

        def parse(i: int, chunk: int) -> bool:
            if i == n:
                return chunk == 0

            byte = data[i]
            if chunk == 0:
                if byte & l1 == 0:
                    return parse(i + 1, 0)
                else:
                    mask = l1
                    chunk_count = 0
                    while mask and byte & mask == mask:
                        mask >>= 1
                        chunk_count += 1
                    if chunk_count < 2 or chunk_count > 4:
                        return False
                    return parse(i + 1, chunk_count - 1)
            else:
                if not (byte & l1 == l1 and byte & l2 == 0):
                    return False
                return parse(i + 1, chunk - 1)

        return parse(0, 0)

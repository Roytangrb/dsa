# Author: RT
# Date: 2023-03-20T14:02:40.758Z
# URL: https://leetcode.com/problems/can-place-flowers/


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i, fb in enumerate(flowerbed):
            left = flowerbed[i - 1] if i > 0 else 0
            right = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if left == fb == right == 0:
                flowerbed[i] = 1
                count += 1

            if count >= n:
                return True

        return False

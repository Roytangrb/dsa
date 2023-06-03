# Author: RT
# Date: 2023-06-03T22:59:18.703Z
# URL: https://leetcode.com/problems/design-parking-system/description/


from collections import Counter


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.vacancies = Counter({1: big, 2: medium, 3: small})

    def addCar(self, carType: int) -> bool:
        if self.vacancies[carType] > 0:
            self.vacancies[carType] -= 1
            return True

        return False

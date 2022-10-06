# Author: RT
# Date: 2022-10-06T15:16:22.797Z
# URL: https://leetcode.com/problems/time-based-key-value-store/


from collections import defaultdict
from sortedcontainers import SortedKeyList


class TimeMap:
    """Used sortedcontainers to handle timestamp in arbitrary order"""

    def __init__(self):
        self.mp = defaultdict(lambda: SortedKeyList(key=lambda x: x[0]))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        if not values or timestamp < values[0][0]:
            return ""

        i = values.bisect_key_left(timestamp)
        if i == len(values):
            return values[-1][1]
        elif values[i][0] == timestamp:
            return values[i][1]
        else:
            return values[i - 1][1]

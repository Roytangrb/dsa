# Author: RT
# Date: 2022-08-06T15:02:20.933Z
# URL: https://leetcode.com/problems/poor-pigs/


import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # number of states per pig can be after given rounds of test
        # round 0 - [alive]
        # round 1 = [alive, die]
        # round 2 = [alive, die at 1st round, die at 2nd round]
        # ...
        rounds = minutesToTest // minutesToDie
        states = rounds + 1
        # x pig with s possible states, the number of buckets could be tested:
        # math.pow(s, x). Find smallest x such that s ** x >= buckets
        # xlog(s) = log(buckets)
        return math.ceil(math.log(buckets) / math.log(states))

# Author: RT
# Date: 2023-01-07T14:28:12.972Z
# URL: https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        total_gas = tank = total_cost = 0
        starting = 0

        for i in range(n):
            if tank < 0:
                starting = i
                tank = 0
            total_cost += cost[i]
            total_gas += gas[i]
            tank += gas[i] - cost[i]

        return -1 if total_gas < total_cost else starting

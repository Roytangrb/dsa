# Author: RT
# Date: 2022-12-20T14:11:57.244Z
# URL: https://leetcode.com/problems/keys-and-rooms/


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        keys = {0}
        q = [0]
        visited = {0}
        while q:
            nq = []
            for room in q:
                keys.update(rooms[room])
                for room_with_key in rooms[room]:
                    if room_with_key not in visited:
                        visited.add(room_with_key)
                        nq.append(room_with_key)

            q = nq

        return len(visited) == n

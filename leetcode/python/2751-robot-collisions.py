# Author: RT
# Date: 2023-06-25T04:19:04.854Z
# URL: https://leetcode.com/problems/robot-collisions/


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        t = 0
        stack = []
        for pos, hp, d, rid in sorted(
            zip(positions, healths, directions, range(len(positions))),
            key=lambda x: x[0],
        ):
            if not stack:
                stack.append([pos, hp, d, rid])
                continue

            if d == stack[-1][2]:
                stack.append([pos, hp, d, rid])
                continue
            else:
                if d == "L":
                    removed = False
                    while stack and stack[-1][2] != d:
                        if pos - t <= stack[-1][0] + t:
                            if hp < stack[-1][1]:
                                stack[-1][1] -= 1
                                removed = True
                                break
                            elif hp > stack[-1][1]:
                                stack.pop()
                                hp -= 1
                            else:
                                stack.pop()
                                removed = True
                                break
                        else:
                            t += (pos - stack[-1][0]) / 2

                    if not removed:
                        stack.append([pos, hp, d, rid])
                if d == "R":
                    removed = False
                    while stack and stack[-1][2] != d:
                        if pos + t <= stack[-1][0] - t:
                            if hp < stack[-1][1]:
                                stack[-1][1] -= 1
                                removed = True
                                break
                            elif hp > stack[-1][1]:
                                stack.pop()
                                hp -= 1
                            else:
                                stack.pop()
                                removed = True
                                break
                        else:
                            break

                    if not removed:
                        stack.append([pos, hp, d, rid])

        return [x[1] for x in sorted(stack, key=lambda x: x[3])]

# Author: RT
# Date: 2023-07-13T23:10:11.531Z
# URL: https://leetcode.com/problems/course-schedule/


from collections import defaultdict


class Solution:
    def canfinish(self, numcourses: int, prerequisites: list[list[int]]) -> bool:
        radj = defaultdict(list)
        deps_count = Counter()
        # b is prerequisite of a
        for a, b in prerequisites:
            radj[b].append(a)
            deps_count[a] += 1

        can_take = []
        for course in range(numCourses):
            if not deps_count[course]:
                can_take.append(course)

        taken = 0
        while can_take:
            new_can_take = []

            for to_take in can_take:
                taken += 1
                for course in radj[to_take]:
                    deps_count[course] -= 1
                    if deps_count[course] == 0:
                        new_can_take.append(course)

            can_take = new_can_take

        return taken == numCourses

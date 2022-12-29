# Author: RT
# Date: 2022-12-29T12:38:04.444Z
# URL: https://leetcode.com/problems/single-threaded-cpu/


import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)
        ans = []
        tasks = sorted(
            ((task[0], task[1], task_id) for task_id, task in enumerate(tasks)),
            reverse=True,
            key=lambda x: x[0],
        )
        q = []
        t = 0
        while len(ans) < n:
            while tasks and tasks[-1][0] <= t:
                _, process_time, task_id = tasks.pop()
                heapq.heappush(q, (process_time, task_id))

            if not q:
                t = tasks[-1][0]
                continue

            process_time, task_id = heapq.heappop(q)
            t += process_time
            ans.append(task_id)

        return ans

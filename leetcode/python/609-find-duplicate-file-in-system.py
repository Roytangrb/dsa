# Author: RT
# Date: 2022-09-19T12:57:19.545Z
# URL: https://leetcode.com/problems/find-duplicate-file-in-system/


from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_fp_map = defaultdict(list)

        for path in paths:
            directory, files = path.split(" ", 1)
            for file in files.split(" "):
                i = len(file) - 1
                while file[i] != "(":
                    i -= 1
                content = file[i + 1 : len(file) - 1]
                content_fp_map[content].append(directory + "/" + file[:i])

        return [v for v in content_fp_map.values() if len(v) > 1]

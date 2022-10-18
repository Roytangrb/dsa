# Author: RT
# Date: 2022-10-18T14:07:17.396Z
# URL: https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return self.say(self.countAndSay(n - 1))

    def say(self, s: str) -> str:
        prev = ""
        count = 0
        out = ""
        for c in s:
            if c != prev:
                out += f"{count}{prev}" if count else ""
                count = 1
                prev = c
            else:
                count += 1

        if count:
            out += f"{count}{prev}"

        return out

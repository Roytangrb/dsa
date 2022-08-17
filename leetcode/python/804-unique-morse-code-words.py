# Author: RT
# Date: 2022-08-17T15:41:37.894Z
# URL: https://leetcode.com/problems/unique-morse-code-words/


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        encodings = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len(
            set("".join([encodings[ord(c) - ord("a")] for c in word]) for word in words)
        )

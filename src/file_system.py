"""Simulate file system

https://leetcode.com/problems/design-file-system/
"""

from typing import Optional

from data_structures.trie import TrieNode


class FileSystem:
    def __init__(self):
        self.trie = TrieNode()

    def cd(self, *dirs) -> Optional[dict]:
        """Search a path in trie, return children mapping if found"""
        t = self.trie.mp
        for d in dirs:
            if d not in t:
                return None
            t = t[d].mp

        return t

    def create_path(self, path: str, value: int) -> bool:
        """Create given path with associated value

        Returns:
            - True: if path created
            - False: if path already exists or path to parent does not exist
        """
        *dirs, last = path.removeprefix("/").split("/")
        parent = self.cd(*dirs)

        if not parent or last in parent:
            return False

        parent[last] = TrieNode({}, value)
        return True

    def get(self, path: str) -> int:
        """Get value associated with given path

        Returns:
            -1: if path does not exist
            val (int): value at path
        """
        *dirs, last = path.removeprefix("/").split("/")
        parent = self.cd(*dirs)

        if not parent or last not in parent:
            return -1

        return parent[last].val


if __name__ == "__main__":
    fs = FileSystem()
    assert (fs.create_path("/a", 1), fs.get("/a")) == (True, 1)

    fs = FileSystem()
    assert (
        fs.create_path("/a", 1),
        fs.create_path("/a/b", 2),
        fs.get("/a/b"),
        fs.get("/a/c"),
        fs.create_path("/c/d", 3),
        fs.get("/c"),
    ) == (True, True, 2, -1, False, -1)

"""Utility data types for trie"""

from typing import Optional


class TrieNode:
    mp: dict[str, "TrieNode"]
    val: Optional[int] = None

    def __init__(
        self, mp: Optional[dict[str, "TrieNode"]] = None, val: Optional[int] = None
    ) -> None:
        self.mp = mp or {}
        self.val = val

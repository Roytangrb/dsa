from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None

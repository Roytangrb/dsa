from dataclasses import dataclass, field
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


@dataclass
class NaryTreeNode:
    val: int
    children: list = field(default_factory=list)
    subtree_size: int = 0

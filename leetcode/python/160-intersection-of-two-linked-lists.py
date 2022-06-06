# Author: RT
# Date: 2022-06-06T15:06:19.365Z
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """Two pass, first pass to find difference between longer list and shorter list"""
        a, b = headA, headB
        while a and b:
            a = a.next
            b = b.next

        shorter, longer = (headA, headB) if a is None else (headB, headA)
        remain = a or b

        while remain:
            remain = remain.next
            longer = longer.next

        while shorter and longer:
            if shorter is longer:
                return shorter
            shorter = shorter.next
            longer = longer.next

        return None

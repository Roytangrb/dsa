# Author: RT
# Date: 2022-07-22T14:24:10.913Z
# URL: https://leetcode.com/problems/partition-list/


from collections import deque
from typing import Optional

from .types import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # lomuto partition (not stable)
        i = j = head
        tail = deque()
        while j:
            if j.val < x:
                i.val, j.val = j.val, i.val
                i = i.next
            else:
                tail.append(j.val)
            j = j.next

        # restore the original order of positions [i:]
        while i:
            i.val = tail.popleft()
            i = i.next

        return head

    def partition_two_ptr(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # concat node to 2 dummy head, join after iterating all
        prefix = pnode = ListNode(0)
        suffix = snode = ListNode(0)

        while head:
            if head.val < x:
                pnode.next = head
                pnode = pnode.next
            else:
                snode.next = head
                snode = snode.next
            head = head.next

        # snode is still pointing to last node >= x, break cycle in the concat list
        snode.next = None
        # join prefix with suffix
        pnode.next = suffix.next

        return prefix.next

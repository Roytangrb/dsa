# Author: RT
# Date: 2022-09-28T14:52:03.777Z
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from .types import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return

        target_prev = None
        target = head
        offset = head
        for _ in range(n):
            offset = offset.next
        while offset:
            offset = offset.next
            target_prev = target
            target = target.next
        if target_prev:
            target_prev.next = target.next
        else:
            return target.next

        return head

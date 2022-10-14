# Author: RT
# Date: 2022-10-14T14:47:00.802Z
# URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from .types import ListNode


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next
            del slow

            return head

        return None

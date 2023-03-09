# Author: RT
# Date: 2023-03-09T14:20:36.357Z
# URL: https://leetcode.com/problems/linked-list-cycle-ii/


from .types import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        seen = set()

        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next

        return None

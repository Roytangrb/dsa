# Author: RT
# Date: 2022-12-06T14:32:16.854Z
# URL: https://leetcode.com/problems/odd-even-linked-list/


from .types import ListNode


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        even_head = head.next

        odd = head
        even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

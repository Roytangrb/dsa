# Author: RT
# Date: 2022-12-05T12:10:44.056Z
# URL: https://leetcode.com/problems/middle-of-the-linked-list/


from .types import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

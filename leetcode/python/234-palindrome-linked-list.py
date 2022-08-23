# Author: RT
# Date: 2022-08-23T13:26:14.474Z
# URL: https://leetcode.com/problems/palindrome-linked-list/


from .types import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        """Reverse second half in-place and two-pointers compare"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        front, rear = head, self.reverse(slow)
        while rear:
            if front.val != rear.val:
                return False
            front = front.next
            rear = rear.next

        return True

    def reverse(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

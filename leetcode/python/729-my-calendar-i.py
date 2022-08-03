# Author: RT
# Date: 2022-08-03T14:16:04.656Z
# URL: https://leetcode.com/problems/my-calendar-i/


from dataclasses import dataclass


@dataclass
class ListNode:
    start: int
    end: int
    next: "ListNode" | None = None


class MyCalendar:
    """Linked-List implementation

    TODO: Balanced Tree implementation
    """

    def __init__(self):
        self.bookings = ListNode(0, 0)

    def book(self, start: int, end: int) -> bool:
        node = self.bookings
        while node:
            if start >= node.end and (not node.next or end <= node.next.start):
                temp = node.next
                node.next = ListNode(start, end)
                node.next.next = temp
                return True

            if start < node.end:
                return False

            node = node.next

        return False

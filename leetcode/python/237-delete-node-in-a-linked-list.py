# Author: RT
# Date: 2022-10-13T13:50:26.379Z
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/

from .types import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        # node is guaranteed not the last one
        node.val = node.next.val
        node.next = node.next.next

    def deleteNode_On(self, node: ListNode):
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next

        prev.next = None

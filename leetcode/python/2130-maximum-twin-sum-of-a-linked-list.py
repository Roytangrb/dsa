# Author: RT
# Date: 2023-05-17T04:33:13.870Z
# URL: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


from .types import ListNode


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        """O(1) space and O(n) time complexity"""
        if not head:
            return 0

        slow = head
        fast = head.next
        slow_prev = None
        while fast and fast.next:
            temp = slow.next
            fast = fast.next.next
            # reverse the first half to optimize space
            slow.next = slow_prev
            slow_prev = slow
            slow = temp

        # slow is the left-median
        l1, l2 = slow, slow.next
        l1.next = slow_prev
        ans = 0

        while l1:
            ans = max(ans, l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next

        return ans

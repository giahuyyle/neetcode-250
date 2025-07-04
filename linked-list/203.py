# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode
from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy

        while prev:
            while prev.next and (prev.next.val == val):
                prev.next = prev.next.next
            prev = prev.next

        return dummy.next
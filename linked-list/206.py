# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None

        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        
        return dummy
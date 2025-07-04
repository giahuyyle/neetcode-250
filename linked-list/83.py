# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        if head:
            nex = head.next

        while head and nex:
            if head.val == nex.val:
                head.next = nex.next
            else:
                head = head.next
            nex = head.next
        
        return dummy
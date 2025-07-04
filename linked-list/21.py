from ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = ListNode()

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            dummy.next = list1
        else:
            dummy.next = list2
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next
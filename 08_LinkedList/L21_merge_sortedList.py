# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergeList=ListNode(-101)
        temp=mergeList
        ptr1 = list1
        ptr2 = list2

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val<=ptr2.val:
                temp.next=ptr1
                ptr1=ptr1.next
                temp=temp.next
            else:
                temp.next=ptr2
                ptr2=ptr2.next
                temp=temp.next
        while ptr1 is not None:
            temp.next=ptr1
            ptr1=ptr1.next
            temp=temp.next
        
        while ptr2 is not None:
            temp.next=ptr2
            ptr2=ptr2.next
            temp=temp.next
        
        return mergeList.next
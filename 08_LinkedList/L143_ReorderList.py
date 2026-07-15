# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        def reverseList(head):
            curr=head
            prev=None
            next=None
            while curr!=None:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        
        #dividing list into two halves
        slow=head
        fast=head

        FirstList=head

        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next

        secList=slow.next
        slow.next=None
        secList=reverseList(secList)

        #joining the lists alternatively
        while FirstList is not None and secList is not None:
            next1=FirstList.next
            next2=secList.next
            FirstList.next=secList
            FirstList=next1
            secList.next=FirstList
            secList=next2


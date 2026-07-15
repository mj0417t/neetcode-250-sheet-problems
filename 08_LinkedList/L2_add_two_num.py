# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2=l1,l2
        res=ListNode(-1)
        temp=res
        carry=0
        while p1 and p2:
            s=p1.val+p2.val+carry
            carry=s//10
            temp.next=ListNode(s%10)
            temp=temp.next
            p1=p1.next
            p2=p2.next
        while p1:
            s=p1.val+carry
            carry=s//10
            temp.next=ListNode(s%10)
            temp=temp.next
            p1=p1.next
        while p2:
            s=p2.val+carry
            carry=s//10
            temp.next=ListNode(s%10)
            temp=temp.next
            p2=p2.next
        if carry:
            temp.next=ListNode(carry)
            

        return res.next
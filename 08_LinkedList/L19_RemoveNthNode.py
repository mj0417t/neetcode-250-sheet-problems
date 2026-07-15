# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        k=head
        for i in range(n):
            k=k.next
        if not k:
            head=head.next
        else:
            while k.next is not None:
                curr=curr.next
                k=k.next
            curr.next=curr.next.next
        return head
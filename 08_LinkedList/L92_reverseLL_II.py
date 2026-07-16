# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if head.next is None:
        #     return head
        # if left==right:
        #     return head
        # def reverse(head):
        #     curr=head
        #     prev=None
        #     next=None
        #     while curr:
        #         next=curr.next
        #         curr.next=prev
        #         prev=curr
        #         curr=next
        #     return prev
        
        # # Dummy node
        # dummy = ListNode(0)
        # dummy.next = head

        # curr=head
        # leftNode=dummy
        # leftNode.next = head


        # for i in range(1,left):
        #     leftNode=curr
        #     curr=curr.next

        # start =curr
        # for i in range(left,right):
        #     curr=curr.next
        # rightNode=curr.next

        # curr.next=None


        # leftNode.next=reverse(start)
        
        # start.next=rightNode

        # return dummy.next

        if not head or left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for _ in range(left-1):
            prev=prev.next
        
        curr=prev.next

        for _ in range(right-left):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=tmp
        return dummy.next
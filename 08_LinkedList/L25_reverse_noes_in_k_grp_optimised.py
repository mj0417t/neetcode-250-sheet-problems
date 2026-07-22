# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grp_prev=dummy
        while True:
            kth= self.getKth(grp_prev,k)
            if not kth:
                break
            grp_nxt=kth.next
            prev,curr=kth.next,grp_prev.next
            while curr!=grp_nxt:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=grp_prev.next
            grp_prev.next=kth
            grp_prev=tmp

        return dummy.next
    def getKth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
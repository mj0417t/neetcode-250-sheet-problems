# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        curr=head
        lst=[]
        i=0
        while curr:
            i+=1
            lst.append(curr.val)
            if i%k==0:
                res.append(lst)
                lst=[]
            curr=curr.next
        ans=[]
        for ls in res:
            ans.append(ls[::-1])
        print(ans,lst)
        ans.append(lst)
        print(ans)
        dum=ListNode(0)
        head=dum
        for lst in ans:
            for i in range(len(lst)):
                dum.next= ListNode(lst[i])
                dum=dum.next
        return head.next
    

head = [1,2,3,4,5]
k = 2
hd=ListNode(0)
cur=hd
for val in head:
    cur.next=ListNode(val)
sol=Solution()
hd=sol.reverseKGroup(hd.next,k)


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList=Node(-100001)
        temp=newList
        curr=head
        while curr is not None:
            temp.next=Node(curr.val)
            curr=curr.next
        newList=newList.next
        temp=newList
        curr=head
        while curr is not None:
            newList.next=Node(curr.val)
            curr=curr.next
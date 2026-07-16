
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None
        
        # newList=Node(-100001)
        # temp=newList
        # curr=head
        # nodeMap ={}
        # while curr is not None:
        #     temp.next=Node(curr.val)
        #     nodeMap[curr]=temp.next
        #     curr=curr.next
        #     temp=temp.next
        # curr=head
        # temp=newList.next
        # while curr is not None:
        #     temp.random=nodeMap.get(curr.random)
        #     curr=curr.next
        #     temp=temp.next
        
        # return newList.next

        #using interleaving method

        curr=head
        while curr:
            copy=Node(curr.val)
            copy.next=curr.next
            curr.next=copy
            curr=copy.next
        
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next

        curr=head
        copyhead=head.next
        while curr:
            copy=curr.next
            curr.next=copy.next
            if copy.next:
                copy.next=copy.next.next
            curr=curr.next
        return copyhead

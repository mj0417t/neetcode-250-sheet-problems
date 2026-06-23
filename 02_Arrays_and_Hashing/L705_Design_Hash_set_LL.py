class ListNode:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None

class MyHashSet:

    def __init__(self):
        self.bucket=[ListNode(0) for _ in range(10000)]
        

    def add(self, key: int) -> None:
        curr=self.bucket[key%len(self.bucket)]
        while curr.next:
            if curr.next.data ==key:
                return
            curr=curr.next
        curr.next=ListNode(key)

    def remove(self, key: int) -> None:
        curr=self.bucket[key%len(self.bucket)]
        while curr.next:
            if curr.next.data ==key:
                curr.next=curr.next.next
                return
            curr=curr.next
        

    def contains(self, key: int) -> bool:
        curr=self.bucket[key%len(self.bucket)]
        while curr.next:
            if curr.next.data ==key:
                return True
            curr=curr.next
        return False
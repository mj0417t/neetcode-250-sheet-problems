class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.count=0
        self.k=k
        self.head=None
        self.tail=None

    def enQueue(self, value: int) -> bool:
        if self.count==self.k:
            return False
        newNode=ListNode(value)
        if not self.count:
            self.head=self.tail=newNode
            newNode.next=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
        
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if not self.count:
            return False
        if self.count==1:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        self.count-=1
        return True
    

        

    def Front(self) -> int:
        if self.count:
            return self.head.val
        return -1
    
        

    def Rear(self) -> int:
        if self.count:
            return self.tail.val
        return -1
    

    def isEmpty(self) -> bool:
        return self.count==0
        

    def isFull(self) -> bool:
        return self.count==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(4)
param_4 = obj.Rear()
param_6 = obj.isFull()
param_2 = obj.deQueue()
param_1 = obj.enQueue(4)
param_3 = obj.Front()
param_5 = obj.isEmpty()
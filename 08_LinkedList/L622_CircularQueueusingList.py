class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0      # index of first element
        self.rear = 0       # index where next element will be inserted
        self.count = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.count==self.k:
            return False
        self.queue[self.rear]=value
        self.rear=(self.rear+1)%self.k
        self.count+=1
        return True
        

    def deQueue(self) -> bool:
        if self.count==0:
            return False
        self.front=(self.front+1)%self.k
        self.count-=1
        return True
        

    def Front(self) -> int:
        if self.count:
            return self.queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if self.count:
            return self.queue[(self.rear-1+self.k)%self.k]
        return -1

    def isEmpty(self) -> bool:
        return  self.count==0
        

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
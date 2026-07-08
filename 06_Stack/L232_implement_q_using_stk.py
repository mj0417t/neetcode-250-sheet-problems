class MyQueue:

    # def __init__(self):
    #     self.st1=[]
    #     self.st2=[]
        

    # def push(self, x: int) -> None:
    #     while self.st1:
    #         self.st2.append(self.st1.pop())
    #     self.st1.append(x)
    #     while self.st2:
    #         self.st1.append(self.st2.pop())
        

    # def pop(self) -> int:
    #     return self.st1.pop()
        

    # def peek(self) -> int:
    #     return self.st1[-1]
        

    # def empty(self) -> bool:
    #     return not self.st1

    def __init__(self):
        self.in_stk=[]
        self.out_stk=[]
        

    def push(self, x: int) -> None:
        self.in_stk.append(x)
            
    def pop(self) -> int:
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk.pop()
        

    def peek(self) -> int:
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
        

    def empty(self) -> bool:
        return not self.in_stk and not self.out_stk
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
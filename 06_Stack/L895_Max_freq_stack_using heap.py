class FreqStack:

    def __init__(self):
        self.st=[]
        self.cnt={}
        

    def push(self, val: int) -> None:
        self.st.append(val)
        self.cnt[val]=1+self.cnt.get(val,0)
        

    def pop(self) -> int:
        maxCnt=max(self.cnt.values())
        i=len(self.st)-1
        while self.cnt[self.st[i]]!=maxCnt:
            i-=1
        self.cnt[self.st[i]]-=1
        return self.st.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
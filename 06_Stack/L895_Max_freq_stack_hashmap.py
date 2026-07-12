import heapq
class FreqStack:

    def __init__(self):
        self.stacks={}
        self.cnt={}
        self.maxCnt=0

    def push(self, val: int) -> None:
        valcnt=1+self.cnt.get(val,0)
        self.cnt[val]=valcnt
        if valcnt>self.maxCnt:
            self.maxCnt=valcnt
            self.stacks[valcnt]=[]
        self.stacks[valcnt].append(val)

    def pop(self) -> int:
        res=self.stacks[self.maxCnt].pop()
        self.cnt[res]-=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
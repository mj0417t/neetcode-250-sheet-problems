from collections import defaultdict
class ListNode:
    def __init__(self,key:int, value:int):
        self.key=key
        self.value=value
        self.freq=1
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.size=0

    def length(self):
        return self.size
    
    def pushRight(self, node):
        prev=self.right.prev
        node.next=self.right
        node.prev=prev
        prev.next=node
        self.right.prev=node
        self.size+=1

    def pop(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        node.prev=None
        node.next=None
        self.size-=1

    def popLeft(self):
        if self.length()==0:
            return None
        node=self.left.next
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.lfuCnt=0
        self.nodeMap={}
        self.freqListMap=defaultdict(LinkedList)

    def counter(self, node):
        cnt=node.freq
        self.freqListMap[cnt].pop(node)

        if cnt==self.lfuCnt and self.freqListMap[cnt].length()==0:
            self.lfuCnt+=1
        node.freq+=1
        self.freqListMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node=self.nodeMap[key]
        self.counter(node)
        return node.value
    

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.nodeMap:
            node=self.nodeMap[key]
            node.value=value
            self.counter(node)
            return
        
        if len(self.nodeMap)==self.cap:
            node=self.freqListMap[self.lfuCnt].popLeft()
            del self.nodeMap[node.key]
        node=ListNode(key,value)
        self.nodeMap[key]=node
        self.freqListMap[1].pushRight(node)
        self.lfuCnt=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self,key:int,val:int):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev

    def insert(self,node):
        prev=self.right.prev
        next=self.right
        prev.next=node
        next.prev=node
        node.next=next
        node.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


lRUCache = LRUCache(2)
lRUCache.put(2,1)
print(lRUCache.cache)
print(lRUCache.get(2))
lRUCache.put(1, 1)   # cache is {1=1}
print(lRUCache.cache)
lRUCache.put(2, 2)   # cache is {1=1, 2=2}
print(lRUCache.cache)
print(lRUCache.get(1))      # return 1
lRUCache.put(3, 3)   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.cache)
print(lRUCache.get(2))   # returns -1 (not found)
lRUCache.put(4, 4)   #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.cache)
print(lRUCache.get(1))      # return -1 (not found)
print(lRUCache.get(3))      #  return 3
print(lRUCache.get(4))      # return 4
 
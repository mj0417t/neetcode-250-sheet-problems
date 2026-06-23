
class MyHashSet:

    def __init__(self):
        self.buck=[0]*31251
        
    def getMask(self, key):
        return 1<<(key%32)
    
    def add(self, key: int) -> None: 
        self.buck[key//32] |= self. getMask(key)      

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.buck[key//32] ^= self.getMask(key)
        

    def contains(self, key: int) -> bool:
        return self.buck[key//32] & self.getMask(key)!=0

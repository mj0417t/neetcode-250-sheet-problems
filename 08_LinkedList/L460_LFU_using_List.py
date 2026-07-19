class LFUCache:

    def __init__(self, capacity: int):
        self.cache=[]
        self.cap=capacity


    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                tmp=self.cache.pop(i)
                tmp[2]+=1
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                tmp=self.cache.pop(i)
                tmp[1]=value
                tmp[2]+=1
                self.cache.append(tmp)
                return
        if len(self.cache)>=self.cap:
            self.cache.sort(key=lambda x: x[2])
            self.cache.pop(0)
        self.cache.append([key,value,1])



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
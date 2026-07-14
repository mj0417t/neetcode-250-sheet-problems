from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        vals=self.map.get(key)
        
        l,r=0,len(vals)-1
        ans=''
        while l<=r:
            mid=(l+r)//2
            if vals[mid][1]<=timestamp:
                ans= vals[mid][0]
                l=mid+1
            else:
                r=mid-1
        return ans
    

timeMap = TimeMap()
timeMap.set("love","high",10)
timeMap.set("love","low",20)
print(timeMap.get("love",5))
print(timeMap.get("love",10))
print(timeMap.get("love",15)) 
print(timeMap.get("love",20))
print(timeMap.get("love",25))


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # people.sort()
        #using counting sort 
        cnt=[0]*(limit+1)
        for p in people:
            cnt[p]+=1
        
        idx=0
        i=1
        while idx<len(people):
            while cnt[i]==0:
                i+=1
            people[idx]=i
            cnt[i]-=1
            idx+=1
        boats=0
        l,r=0,len(people)-1
        while l<r:
            if people[l]+people[r]<=limit:
                r-=1
                l+=1
            else:
                r-=1
            boats+=1
        
        if l==r:
            boats+=1

        return boats



if __name__=='__main__':
    people = [3,2,2,1]
    limit = 3
    sol=Solution()
    ans=sol.numRescueBoats(people,limit)
    print(ans)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        maps1={}
        maps2={}
        for i in range(len(s1)):
            maps1[s1[i]]=1 + maps1.get(s1[i],0)
            maps2[s2[i]]=1 + maps2.get(s2[i],0)
        
        if maps1==maps2:
            return True
        l=0
        for r in range(len(s1), len(s2)):
            maps2[s2[l]]-=1
            if maps2[s2[l]]<1:
                del maps2[s2[l]]
            l+=1
            maps2[s2[r]]=1+maps2.get(s2[r],0)

            if maps1==maps2:
                return True
        return False

if __name__=='__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s3="eidboaoo"
    sol=Solution()
    print(sol.checkInclusion(s1,s2))
    print(sol.checkInclusion(s1,s3))
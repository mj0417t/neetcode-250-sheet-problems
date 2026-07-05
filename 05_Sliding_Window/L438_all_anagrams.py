class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        mapS={}
        mapP={}
        res=[]
        for i in range(len(p)):
            mapP[p[i]]=1+mapP.get(p[i],0)
            mapS[s[i]]=1+mapS.get(s[i],0)
        if mapP==mapS:
            res.append(0)
        
        l=0
        for r in range(len(p),len(s)):
            mapS[s[l]]-=1
            if mapS[s[l]]==0:
                del mapS[s[l]]
            l+=1
            mapS[s[r]]=1+mapS.get(s[r],0)
            if mapP==mapS:
                res.append(l)
        return res


if __name__=='__main__':
    s = "cbaebabacd"
    p = "abc"

    s2 = "abab"
    p2 = "ab"

    sol=Solution()
    print(sol.findAnagrams(s,p))
    print(sol.findAnagrams(s2,p2))
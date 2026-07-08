class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT={}
        for i in range(len(t)):
            freqT[t[i]]=1+freqT.get(t[i],0)
        window={}
        res=[-1,-1]
        resLen=float('inf')
        l=0
        have=0
        need=len(freqT)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in freqT and freqT[s[r]]==window[s[r]]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    res=[l,r]
                    resLen=r-l+1
                
                window[s[l]]-=1
                if s[l] in freqT and window[s[l]]<freqT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen != float('inf') else ''
        

        

if __name__=='__main__':
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    s2 = "a"
    t2 = "a"
    s3 = "a"
    t3 = "aa"
    sol=Solution()
    print(sol.minWindow(s1,t1))
    print(sol.minWindow(s2,t2))
    print(sol.minWindow(s3,t3))
    
    
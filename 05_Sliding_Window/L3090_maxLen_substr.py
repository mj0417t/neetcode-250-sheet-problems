class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        charMap=[0]*26
        n=len(s)
        lensub=0
        for r in range(n):
            while charMap[ord(s[r])-97]>=2 and l<n:
                charMap[ord(s[l])-97]-=1
                l+=1
            charMap[ord(s[r])-97]+=1
            lensub=max(lensub,r-l+1)
        return lensub

if __name__=='__main__':
    s1 = "bcbbbcba"
    s2 ="aaaa"
    sol=Solution()
    print(sol.maximumLengthSubstring(s1))
    print(sol.maximumLengthSubstring(s2))
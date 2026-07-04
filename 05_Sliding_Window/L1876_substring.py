from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # n=len(s)
        # if n<3:
        #     return 0
        # cnt=0
        # for i in range(n-2):
        #     charSet=set()
        #     for j in range(i,i+3):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     if len(charSet)==3:
        #         cnt+=1
        # return cnt

        # l=cnt=0
        # charMap=defaultdict(int)
        # for r in range(len(s)):
        #     if r-l>=3:
        #         charMap[s[l]]-=1
        #         if charMap[s[l]]==0:
        #             del charMap[s[l]]
        #         l+=1
        #     charMap[s[r]]+=1
        #     if len(charMap)==3:
        #         cnt+=1
        
            
        # return cnt

        n=len(s)
        cnt=0
        for i in range(n-2):
            if len(set(s[i:i+3]))==3:
                cnt+=1
        return cnt


if __name__=='__main__':
    s1 = "xyzzaz"
    s2= "aababcabc"
    sol=Solution()
    print(sol.countGoodSubstrings(s1))
    print(sol.countGoodSubstrings(s2))
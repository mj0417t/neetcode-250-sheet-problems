class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p=q=0
        res=''
        while p<len(word1) and q<len(word2):
            res+=word1[p]
            res+=word2[q]
            p,q=p+1,q+1
        
        while p<len(word1):
            res+=word1[p]
            p+=1

        while q<len(word2):
            res+=word2[q]
            q+=1
        return res


if __name__=='__main__':
    s = "abca"
    s1="aba"
    sol=Solution()
    print(sol.mergeAlternately(s,s1))
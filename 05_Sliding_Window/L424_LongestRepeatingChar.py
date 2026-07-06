class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet=set(s)
        lens=0
        for char in charSet:
            opt,l=k,0
            for r in range(len(s)):
                if s[r]!=char:
                    opt-=1
                    while opt<0:
                        if s[l]!=char:
                            opt+=1
                        l+=1
                lens=max(lens,r-l+1)
        return lens

if __name__=='__main__':
    s1 = "ABAB"
    k1 = 2
    s2 = "AABABBA"
    k2= 1
    sol=Solution()
    print(sol.characterReplacement(s1,k1))
    print(sol.characterReplacement(s2,k2))
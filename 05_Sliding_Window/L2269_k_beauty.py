class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        beauty=0
        for i in range(len(s)-k+1):
            val=int(s[i:i+k])
            # print(len(s),num,val)
            if val==0:
                continue
            if num%val==0:
                beauty+=1
        return beauty

if __name__=='__main__':
    num = 240
    k = 2
    num2 = 430043
    p = 2
    sol=Solution()
    print(sol.divisorSubstrings(num,k))
    print(sol.divisorSubstrings(num2,p))
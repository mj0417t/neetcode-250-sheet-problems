import math
class Solution:
    def cnt_digit(self,n):
        # cnt=0
        # while n!=0:
        #     n=n//10
        #     cnt+=1
        cnt=int(math.log10(n)+1)
        return cnt

if __name__=='__main__':
    sol=Solution()
    num=1243212
    print(sol.cnt_digit(num))
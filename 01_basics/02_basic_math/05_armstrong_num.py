import math
class Solution:
    def isArmstrong(self, num: int) -> bool:
        # digits=[]
        # dup= num
        # cnt=0
        # while num !=0:
        #     digits.append(num%10)
        #     cnt+=1     
        #     num//=10
        # d_sum=0
        # for i in digits:
        #     d_sum+=i**cnt
        # if d_sum==dup:
        #     return True
        # return False 
        dup= num
        digits=int(math.log10(num)+1)
        sum=0
        while num !=0:
            sum+=(num%10)**digits   
            num//=10
        if sum==dup:
            return True
        return False 

if __name__=='__main__':
    sol=Solution()
    num=153
    print(sol.isArmstrong(num))
    print(sol.isArmstrong(123))
    print(sol.isArmstrong(371))
    print(sol.isArmstrong(37001))
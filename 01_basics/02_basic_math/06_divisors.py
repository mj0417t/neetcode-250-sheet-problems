import math
class Solution:
    def find_divisors(self, num: int) -> list:
        divisors=[]
        # for i in range(1,num+1):
        #     if num%i==0:
        #         divisors.append(i)

        for i in range(1,math.isqrt(num)+1):
            if num%i==0:
                divisors.append(i)
                if i != num//i:
                    divisors.append(num//i)
        return divisors
        

if __name__=='__main__':
    sol=Solution()
    num=153
    print(sol.find_divisors(num))
    print(sol.find_divisors(36))
    print(sol.find_divisors(12))
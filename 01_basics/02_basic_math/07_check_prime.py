import math
class Solution:
    def isPrime(self, x: int) -> bool:
        for i in range(2,math.isqrt(x)+1):
            if x%i==0 or x%(x//i)==0:
                return False
        return True   

if __name__=='__main__':
    sol=Solution()
    num=11
    print(sol.isPrime(num))
    print(sol.isPrime(341))
    print(sol.isPrime(23456))
    print(sol.isPrime(12321))
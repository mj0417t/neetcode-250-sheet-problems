class Solution:
    def reverse(self, x: int) -> int:
        is_neg=True if x<0 else False
        if is_neg:
            x=-1*x
        num=0
        while x!=0:
            rem=x%10
            num=num*10+rem
            x=x//10
        if is_neg:
            num=-1*num
        if num < -(2 ** 31) or num > (2**31)-1:
            return -1
        return num
    
if __name__=='__main__':
    sol=Solution()
    num=-43
    print(sol.reverse(num))
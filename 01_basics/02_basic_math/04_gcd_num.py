class Solution:
    def gcd(self, x: int, y:int) -> int:
        # gcd_num=x if x<y else y
        # while gcd_num >0:
        #     if x%gcd_num==0 and y%gcd_num==0:
        #         return gcd_num
        #     else:
        #         gcd_num-=1
        # return gcd_num
        # if x==0:
        #     return y
        # if x<y :
        #     return self.gcd(y,x)     
        # else:
        #     return self.gcd(x-y,y) 

        while x>0 and y>0:
            if x>y:
                x=x%y
            else:
                y=y%x
        if x==0:
            return y
        return x


if __name__=='__main__':
    sol=Solution()
    a=20
    b=15
    print(sol.gcd(a,b))
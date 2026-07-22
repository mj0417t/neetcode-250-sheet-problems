class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=''
        while columnNumber:
            div=columnNumber//26
            rem=columnNumber%26
            if rem==0:
                rem=26
                div-=1
            res+=chr(rem+ord('A')-1)
            columnNumber=div
        return res[::-1]

if __name__=='__main__':
    sol=Solution()
    print(sol.convertToTitle(1))
    print(sol.convertToTitle(28))
    print(sol.convertToTitle(52))
    print(sol.convertToTitle(701))
    print(sol.convertToTitle(2147483647))
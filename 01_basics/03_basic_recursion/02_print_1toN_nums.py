class Solution:
    def printNum(self,start,num):
        if start>num:
            return
        print(start, end=',')
        return self.printNum(start+1,num)


if __name__=='__main__':
    sol=Solution()
    n=5
    sol.printNum(1,n)
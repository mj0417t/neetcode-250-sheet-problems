class Solution:
    def printNum(self,num):
        if num<1:
            return
        print(num, end=' ')
        return self.printNum(num-1)


if __name__=='__main__':
    sol=Solution()
    n=5
    sol.printNum(n)
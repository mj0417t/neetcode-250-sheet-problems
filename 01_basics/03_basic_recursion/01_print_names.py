class Solution:
    def printNames(self,num):
        if num==0:
            return
        print("Names")
        return self.printNames(num-1)


if __name__=='__main__':
    sol=Solution()
    n=5
    sol.printNames(n)
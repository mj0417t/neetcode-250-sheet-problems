class Solution:
    def fibonacci(self, num):
        if num<=1:
            return num
        last=self.fibonacci(num-1)
        slast=self.fibonacci(num-2)
        return last+slast

if __name__=='__main__':
    sol=Solution()
    n=10
    for i in range(1,n+1):
        print(sol.fibonacci(i), end=" ")
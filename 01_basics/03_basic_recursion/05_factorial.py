class Solution:
    def find_factorial(self,num):
        if num==1:
            return 1
        else:
            return num * self.find_factorial(num-1)


if __name__=='__main__':
    sol=Solution()
    n=5
    print(sol.find_factorial(n))
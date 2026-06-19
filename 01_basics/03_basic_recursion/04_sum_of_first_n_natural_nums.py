class Solution:
    def numSum(self,num):
        # if num<1:
        #     return 0
        # else:
        #     return num + self.numSum(num-1)
        return num*(num+1)//2


if __name__=='__main__':
    sol=Solution()
    n=5
    print(sol.numSum(n))
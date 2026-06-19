# 1      1
# 12    21
# 123  321
# 12344321

class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(2*n):
                if j<=i:
                    print(j+1,end='')
                elif j>=(2*n)-i-1:
                    print(2*n-j,end='')
                else:
                    print(' ', end='')
            print()

if __name__=='__main__':
    sol=Solution()
    n=4
    sol.pattern(n)
# 1
# 01
# 101
# 0101
# 10101

class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(i+1):
                if (i+j)%2==0:
                    print(1, end='')
                else:
                    print(0, end='')
            print()

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(5)

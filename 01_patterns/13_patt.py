# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

class Solution:
    def pattern(self, n):
        k=1
        for i in range(n):
            for j in range(i+1):
                print(k, end=" ")
                k=k+1
            print()

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)


# A
# AB
# ABC
# ABCD
# ABCDE

class Solution:
    def pattern(self, n):
        
        for i in range(n):
            k=65
            for j in range(i+1):
                print(chr(k), end="")
                k+=1
            print()

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)
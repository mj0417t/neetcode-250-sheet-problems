# E
# D E
# C D E
# B C D E
# A B C D E

class Solution:
    def pattern(self, n):
        for i in range(n):
            k=69
            for j in range(i+1):
                
                print(chr(k-i+j), end=" ")

            print()

if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)
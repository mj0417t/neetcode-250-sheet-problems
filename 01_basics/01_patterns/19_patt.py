# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


class Solution:
    # def pattern(self, n):
    #     for i in range(2*n-1):
    #         for j in range(2*n):
    #             if i<n:
    #                 if j<=(n-1-i) or j>n-1+i:
    #                     print('*', end='')
    #                 else:
    #                     print(' ', end='')
    #             else:
    #                 if j<=i-n or j >= 2*n - 1 - (i - n):
    #                     print('*', end='')
    #                 else:
    #                     print(' ', end='')
    #         print()

    def pattern(self, n):
        for i in range(2*n):
            k = i if i < n else 2*n - 1 - i
            for j in range(2*n):
                if j<=n-1-k or j>=n+k:
                    print('*',end='')
                else:
                    print(' ', end='')
            print()



if __name__=='__main__':
    sol=Solution()
    n=5
    sol.pattern(n)